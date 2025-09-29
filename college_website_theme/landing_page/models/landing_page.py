import re
from odoo import models, fields, api


class LandingPage(models.Model):
    _name = "landing.page"
    _description = 'Landing Page Model'

    title = fields.Char('Title', tracking=True, required=True)
    image = fields.Binary(string='Image', attachment=True, required=True)
    placement_image = fields.Binary(string='Placement Image', attachment=True, required=True)
    description = fields.Char('Description', tracking=True, required=True)
