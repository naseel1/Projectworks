from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    x_show_cpa_footer = fields.Boolean(
        string="Show CPA Footer",
        default=True,
        help="Toggle visibility of the custom footer on this website."
    )
