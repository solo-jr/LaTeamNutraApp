# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ltnConfigSettings(models.Model):
    _name = 'ltn.config.settings'
    _description = 'SettingS La Team Nutra'

    @api.model
    def init_setting(self):
        company_model_data = self.env['ir.model.data'].search([('module', '=', 'base'), ('name', '=', 'main_company')])
        if company_model_data:
            company_model_data.write({'noupdate': False})

    @api.model
    def set_config(self, vals):
        config_setting = self.env['res.config.settings']
        defaults_setting = config_setting.default_get(list(config_setting.fields_get()))
        defaults_setting.update(vals)
        config_setting.create(defaults_setting).execute()

