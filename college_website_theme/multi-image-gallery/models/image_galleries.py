from odoo import models, fields


class ImageGalleries(models.Model):
    _name = "image.galleries"
    _description = 'Image Gallery'

    name = fields.Char('Gallery Name', tracking=True)
    date = fields.Date('Date')
    image_ids = fields.One2many('image.gallery.image', 'gallery_id', string="Images")


class GalleryImage(models.Model):
    _name = 'image.gallery.image'
    _description = 'Gallery Image'

    gallery_id = fields.Many2one('image.galleries', string='Gallery', ondelete='cascade')
    image = fields.Binary(string='Image', attachment=True, required=True)
    name = fields.Char(string='Image Name')
