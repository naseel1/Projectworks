from odoo import models, fields


class GallerySection(models.Model):
    _name = "gallery.section"
    _description = "Gallery Section"

    visitor_name = fields.Char('Name', tracking=True, required=True)
    gallery_image = fields.Binary(string="Image", attachment=True, required=True)
    gallery_description = fields.Char('Description', tracking=True, required=True)
