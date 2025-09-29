from odoo import models, fields


class SsrPricePlan(models.Model):
    _name = "ssr.plan"
    _description = "SSR Plan"

    name = fields.Char(string="Plan Name", required=True)
    plan_type = fields.Selection([
        ('basic_plan', 'Basic Plan'),
        ('essential_plan', 'Essential Plan'),
        ('pro_plan', 'Pro Plan')
    ], string="Plan Type", required=True)
    price = fields.Integer(string="Price", required=True)
    total_price = fields.Integer(string="Total Price (Incl. GST)", required=True)
    plan_points = fields.Html(string="Plan Points")
