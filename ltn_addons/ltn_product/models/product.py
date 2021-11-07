# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    promises = fields.Text("promises")
    capacity = fields.Text("Capacity")
    nutritional_info = fields.Text("Nutritional information")
    usage_tips = fields.Text("Usage tips")
    list_of_ingredients = fields.Text("List of ingredients")
    precaution_for_use = fields.Text("Precaution for use")
    thematic_ids = fields.Many2many('ltn.thematic')
    ltn_customer_ids = fields.Many2many('res.partner', 'ltn_product_customer_rel', 'product_id', 'partner_id',
                                        string='Customers')
    is_favorite = fields.Boolean("Favorite", compute='_compute_favori', search='_search_fav')
    # is_favorite = fields.Boolean("Favorite", readonly=True, store=True)

    def _search_fav(self, op, val):
        # if op in ['=', '!=']
        in_favorite = self.env['ltn.favorites'].search([('user_id', '=', self.env.user.id)])
        if (op == '=' and val) or (op == '!=' and not val):
            return [('id', 'in', in_favorite.name.ids)]
        elif (op == '!=' and val) or (op == '=' and not val):
            return [('id', 'not in', in_favorite.name.ids)]

    def _compute_favori(self):
        for pt in self:
            in_favorite = self.env['ltn.favorites'].search([('name', '=', pt.id), ('user_id', '=', self.env.user.id)])
            if in_favorite:
                pt.is_favorite = True
            else:
                pt.is_favorite = False

    def put_in_my_favorites(self):
        for pt in self:
            self.env['ltn.favorites'].create({
                'name': pt.id,
                'user_id': self.env.user.id,
            })

    def remove_in_my_favorites(self):
        for pt in self:
            in_favorite = self.env['ltn.favorites'].search([('name', '=', pt.id), ('user_id', '=', self.env.user.id)])
            if in_favorite:
                in_favorite.unlink()

    def get_my_favory(self):
        return self.search([('is_favorite', '=', True)])

    def action_send_mail_favorites(self):
        report_name = 'ltn_product.ltn_product_report_envelope'
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        favorites = self.get_my_favory()
        favorites_ids = favorites.ids if favorites else []
        pdf_bin, _ = report._render_qweb_pdf(favorites_ids)
        attachment = self.env['ir.attachment'].create({
            'name': 'La Team Nutra: Product',
            'datas': base64.b64encode(pdf_bin),
            'res_model': 'product.template',
            'type': 'binary',
        })
        context = {
            'default_template_id': self.env.ref('ltn_product.ltn_product_send_mail_mail_template').id,
            'default_model': 'product.template',
            'default_res_id': favorites_ids[0],
            'default_use_template': True,
            'default_composition_mode': 'comment',
            'default_attachment_ids': [(6, 0, attachment.ids)],
            'mark_so_as_sent': True,
            'force_email': True,
        }
        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': context,
        }
        return action


