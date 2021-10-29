# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def get_products(self):
        kanban_view_id = self.env.ref('ltn_product.product_template_ltn_kanban_view').id
        action = {
            'name': self.name,
            "type": "ir.actions.act_window",
            "res_model": "product.template",
            'view_mode': 'kanban,tree,form',
            "views": [[kanban_view_id, "kanban"], [False, "form"], [False, "tree"]],
            "domain": [['ltn_customer_ids', 'in', self.id]],
            "context": {"create": False},
        }
        return action


