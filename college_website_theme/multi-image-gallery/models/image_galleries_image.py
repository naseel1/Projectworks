from odoo import models, fields


class GalleryImage(models.Model):
    _name = 'image.gallery.image'
    _description = 'Gallery Image'

    gallery_id = fields.Many2one('image.galleries', string='Gallery', ondelete='cascade')
    image = fields.Binary(string='Image', attachment=True, required=True)
    name = fields.Char(string='Image Name')
