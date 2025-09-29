from odoo import http
from odoo.http import request


class ImageGalleryController(http.Controller):

    @http.route('/image_gallery', type='http', auth='public', website=True)
    def image_gallery_page(self, **kwargs):
        images = request.env['image.galleries'].sudo().search([], order='date desc')
        return request.render('image-gallery.image_gallery_template', {
            'images': images
        })
