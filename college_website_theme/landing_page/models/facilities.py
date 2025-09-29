from odoo import models, fields


class FacilitiesManage(models.Model):
    _name = "facilities.manage"
    _description = "Simple Facilities"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(string="Facility Name", required=True)
    cover_image = fields.Image(string="Cover Image")
    child_ids = fields.One2many(
        'facilities.sub',
        'parent_id',
        string="Sub Facilities"
    )


class FacilitiesSub(models.Model):
    _name = "facilities.sub"
    _description = "Sub Facility"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(string="Sub Facility Name", required=True)
    description = fields.Text(string="Description")
    parent_id = fields.Many2one(
        'facilities.manage',
        string="Main Facility",
        ondelete='cascade'
    )
    image_ids = fields.One2many(
        'facilities.sub.image',
        'sub_id',
        string="Images"
    )


class FacilitiesSubImage(models.Model):
    _name = "facilities.sub.image"
    _description = "Sub Facility Images"

    sub_id = fields.Many2one(
        'facilities.sub',
        string="Sub Facility",
        ondelete='cascade'
    )
    image = fields.Image(string="Image", required=True)
