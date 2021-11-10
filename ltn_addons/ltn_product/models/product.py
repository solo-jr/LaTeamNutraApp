# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.modules.module import get_resource_path
import base64
import csv
import re
import requests


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    promises = fields.Text("promises")
    capacity = fields.Text("Capacity")
    dosage_for = fields.Text("Dosage for")
    nutritional_info = fields.Text("Nutritional information")
    usage_tips = fields.Text("Usage tips")
    list_of_ingredients = fields.Text("List of ingredients")
    precaution_for_use = fields.Text("Precaution for use")
    thematic_ids = fields.Many2many('ltn.thematic')
    ltn_customer_ids = fields.Many2many('res.partner', 'ltn_product_customer_rel', 'product_id', 'partner_id',
                                        string='Customers')
    is_favorite = fields.Boolean("Favorite", compute='_compute_favori', search='_search_fav')
    adv = fields.Binary('ADV', help="ADV")
    adv_name = fields.Char('ADV Name')
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

    def import_product(self):
        file_name = 'airtable-product.csv'
        full_path_file = get_resource_path('ltn_product', 'data', file_name)
        with open(full_path_file, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            row_index = 2
            product_tmpl_model = self.env['product.template'].sudo()
            partner_model = self.env['res.partner'].sudo()
            thematic_model = self.env['ltn.thematic'].sudo()
            for dict_row in reader:
                dict_real = dict(dict_row)
                # thematic
                thematic_val = {'name': dict_real['Catégorie']}
                thematic = thematic_model.search([('name', '=', thematic_val['name'])], limit=1)
                if not thematic:
                    thematic = thematic_model.create(thematic_val)
                # partner
                partner_val = {
                    'name': dict_real['Client'],
                    'company_type': 'company',
                    'is_custumer_ltn': True,
                }
                partner_img_url = re.sub(r'^.*\((http[^)]+).*$', r'\1', dict_real['Logo blanc']) if dict_real['Logo blanc'] else ''
                if partner_img_url:
                    partner_img_bin = requests.get(partner_img_url)
                    partner_img = base64.b64encode(partner_img_bin.content)
                    partner_val['image_1920'] = partner_img
                partner = partner_model.search([('name', '=', partner_val['name'])], limit=1)
                if not partner:
                    partner = partner_model.create(partner_val)
                else:
                    partner.write(partner_val)
                # product
                product_vals = {
                    'name': dict_real['Produit'],
                    'promises': dict_real['Allégations selectionnées'],
                    'capacity': dict_real['Contenance'],
                    'nutritional_info': dict_real['Composition'],
                    'usage_tips': dict_real['Conseils d\'utilisation'],
                    'list_of_ingredients': dict_real['Liste d\'ingrédients'],
                    'precaution_for_use': dict_real['Précaution d\'emploi'],
                    'dosage_for': dict_real['Dosage pour'],
                    'ltn_customer_ids': [(4, partner.id, 0)],
                    'thematic_ids': [(4, thematic.id, 0)],
                }

                weight = re.sub(r'^([^0-9.]*([0-9.]+)[^0-9.]*)*$', r'\2', dict_real['Poids net'].replace(' ', '').strip().replace(',', '.'))
                if weight:
                    product_vals['weight'] = float(weight)/1000

                img_product_url = re.sub(r'^.*\((http[^)]+).*$', r'\1', dict_real['Mockup-appli']) if dict_real['Mockup-appli'] else ''
                if img_product_url:
                    img = requests.get(img_product_url)
                    image_1920 = base64.b64encode(img.content)
                    product_vals['image_1920'] = image_1920
                adv_url = re.sub(r'^.*\((http[^)]+).*$', r'\1', dict_real['ADV']) if dict_real['ADV'] else ''
                if adv_url:
                    adv_name = re.sub(r'^(.*) *\((http[^)]+).*$', r'\1', dict_real['ADV'])
                    adv_bin = requests.get(adv_url)
                    adv = base64.b64encode(adv_bin.content)
                    product_vals['adv'] = adv
                    product_vals['adv_name'] = adv_name

                product_tmpl = product_tmpl_model.search([('name', '=', product_vals['name']), ('capacity', '=', product_vals['capacity'])], limit=1)
                if not product_tmpl:
                    product_tmpl = product_tmpl_model.create(product_vals)
                else:
                    product_tmpl.write(product_vals)
                self.env.cr.commit()
                row_index += 1
                print(row_index)





