# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'
    rtmg_web_patch_resource_id = fields.Many2one('rtmg.web.patch', string="Web patch", required=True,
        default=lambda self: self.env.ref('rtmg_web_patch.rtmg_web_patch').id)
    rtmg_name = fields.Char("Website global name", related="rtmg_web_patch_resource_id.rtmg_name", readonly=False)
    rtmg_website_signature = fields.Text("Website signature", related="rtmg_web_patch_resource_id.rtmg_website_signature", readonly=False)



