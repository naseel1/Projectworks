from odoo import models, fields, api


class PaymentProviderHDFC(models.Model):
    _name = 'payment.provider_hdfc'
    _description = 'Payment Provider Hdfc'

    def action_do_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_do_draft(self):
        for rec in self:
            rec.state = 'draft'

    hdfc_merchant_id = fields.Char(string="Merchant ID", required=True)
    hdfc_client_id = fields.Char(string="Client ID", required=True)
    api_key = fields.Char(string="API Key", required=True)
    response_key = fields.Char(string="Response Key", required=True)
    base_url = fields.Char(default="https://smartgateway.hdfcbank.com", string="HDFC Base URL")
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed')], string='Status', default='draft')
