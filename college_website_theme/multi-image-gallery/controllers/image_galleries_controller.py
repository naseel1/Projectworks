from odoo import http
from odoo.http import request


class ImageGalleryController(http.Controller):

    @http.route('/image_gallery', type='http', auth='public', website=True)
    def image_gallery_page(self, **kwargs):
        galleries = request.env['image.galleries'].sudo().search([], order='date desc')
        return request.render('multi-image-gallery.multi_image_gallery_template', {
            'galleries': galleries
        })
