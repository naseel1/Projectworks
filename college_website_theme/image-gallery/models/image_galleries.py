from odoo import models, fields
import re


class ImageGalleries(models.Model):
    _name = "image.galleries"
    _description = 'Image Gallery'

    name = fields.Char('Name', tracking=True)
    image = fields.Binary(string="Image", attachment=True)
    date = fields.Date('Date')
