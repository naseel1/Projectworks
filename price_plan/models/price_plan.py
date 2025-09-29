from odoo import models, fields


class PricePlan(models.Model):
    _name = "price.plan"
    _description = "Price Plan"

    name = fields.Char(string="Plan Name", required=True)
    plan_type = fields.Selection([
        ('basic', 'Basic Plan'),
        ('essential', 'Essential Plan'),
        ('pro', 'Pro Plan')
    ], string="Plan Type", required=True)
    price = fields.Float(string="Price", required=True)
    plan_points = fields.Html(string="Plan Points")
