from odoo import models, fields


class FacilitiesManage(models.Model):
    _name = "facility.manage"
    _description = "Simple Facilities"


    name = fields.Char(string="Facility Name", required=True)
    description = fields.Html(string="Description")
    images_ids = fields.One2many(
        'facility.image', 'image_id',
        string="Images"
    )


class FacilitiesImage(models.Model):
    _name = "facility.image"
    _description = "Facility Images"

    image_id = fields.Many2one(
        'facility.manage',
        string="Facility",
        ondelete='cascade'
    )
    image = fields.Binary(string='Image', attachment=True, required=True)
