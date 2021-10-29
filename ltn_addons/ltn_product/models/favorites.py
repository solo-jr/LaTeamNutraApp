# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LtnFavorites(models.Model):
    _name = 'ltn.favorites'
    _description = 'Product Favorites'

    name = fields.Many2one("product.template", string="Product")
    user_id = fields.Many2one("res.users", string="User")
    partner_id = fields.Many2one("res.partner", string="Partner")

    def send_mail(self):
        pass

