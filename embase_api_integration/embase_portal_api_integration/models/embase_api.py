# -*- coding: utf-8 -*-

from odoo import models, fields


class EmbaseAPIConfiguration(models.Model):
    _name = 'embase.api_config'
    _description = 'API Configuration'

    def action_do_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_do_draft(self):
        for rec in self:
            rec.state = 'draft'

    name = fields.Char('Name', required=True)
    base_url = fields.Char('API URL')
    api_token = fields.Char('API Token')
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed')], string='Status', default='draft')
