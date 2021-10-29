# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LtnThematic(models.Model):
    _name = 'ltn.thematic'
    _description = 'Product Thematic'

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Thematic name already exists !"),
    ]

    name = fields.Char("Name")
    image = fields.Image("Image")
    image_128 = fields.Image("Image", related="image")

    def get_products(self):
        kanban_view_id = self.env.ref('ltn_product.product_template_ltn_kanban_view').id
        action = {
            'name': self.name,
            "type": "ir.actions.act_window",
            "res_model": "product.template",
            'view_mode': 'kanban,tree,form',
            "views": [[kanban_view_id, "kanban"], [False, "form"], [False, "tree"]],
            "domain": [['thematic_ids', 'in', self.id]],
            "context": {"create": False},
        }
        return action