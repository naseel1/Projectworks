from odoo import models, fields


class PlacementSection(models.Model):
    _name = "placement.section"
    _description = "Placement Section"

    placement_image = fields.Binary(string="Image", attachment=True, required=True)
