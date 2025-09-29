from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    x_show_popup = fields.Boolean(
        string="Show MES PopUp",
        default=True,
        help="Toggle visibility of the custom footer on this website."
    )
