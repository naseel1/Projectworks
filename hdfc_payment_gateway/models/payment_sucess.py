from odoo import models, fields


# ------------------------------
# SSR Payments
# ------------------------------
class PaymentSSR(models.Model):
    _name = 'payment.ssr'
    _description = 'Payment Success (SSR Registration)'

    order_id = fields.Char(string="Order ID", required=True, index=True)
    amount = fields.Float(string="Amount", required=True)
    customer_id = fields.Char(string="Customer ID", required=True)
    customer_email = fields.Char(string="Customer Email", required=True)
    customer_phone = fields.Char(string="Customer Phone")
    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ], string="Payment Status", default='pending')
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name")
    payment_date = fields.Datetime(string="Payment Date", default=fields.Datetime.now)
    institution_name = fields.Char(string="Institution Name")
    institution_domain = fields.Char(string="Institution Domain")
    sub_domain = fields.Char(string="Subdomain")
    package_prices = fields.Char(string="Package Name")
    address = fields.Text("Address")


# ------------------------------
# Onboarding Payments
# ------------------------------
class PaymentOnboarding(models.Model):
    _name = 'payment.onboarding'
    _description = 'Payment Success (Onboarding Flow)'

    order_id = fields.Char(string="Order ID", required=True, index=True)
    amount = fields.Float(string="Amount", required=True)
    customer_id = fields.Char(string="Customer ID", required=True)
    customer_email = fields.Char(string="Customer Email", required=True)
    customer_phone = fields.Char(string="Customer Phone")
    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ], string="Payment Status", default='pending')
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name")
    payment_date = fields.Datetime(string="Payment Date", default=fields.Datetime.now)
    plan_name = fields.Char(string="Plan Name")
    billedto = fields.Char("Billed To")
    address = fields.Text("Billing Address")
    gstin = fields.Char("GSTIN")
    institution_name = fields.Char(string="Institution Name")
    institution_domain = fields.Char(string="Institution Domain")
    sub_domain = fields.Char(string="Subdomain")
    source_record_id = fields.Char(string="Onboarding Record ID")
