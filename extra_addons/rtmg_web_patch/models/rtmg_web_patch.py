# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RtmgWebPatch(models.Model):
    _name = 'rtmg.web.patch'
    _description = 'rtmg_web_patch.rtmg_web_patch'

    rtmg_name = fields.Char("Website global name")
    rtmg_website_signature = fields.Text("Website signature")

    @api.model
    def get_global_name(self):
        return self.env.ref('rtmg_web_patch.rtmg_web_patch').rtmg_name


