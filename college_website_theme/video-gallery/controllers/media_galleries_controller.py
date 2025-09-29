from odoo import http
from odoo.http import request


class MediaGalleryController(http.Controller):

    @http.route(['/video-gallery'], type='http', auth="public", website=True)
    def media_gallery_page(self, **kwargs):
        media_records = request.env['media.galleries'].sudo().search([], order="date desc")

        return request.render("video-gallery.media_gallery_template", {
            'media_records': media_records
        })
