from odoo import http
from odoo.http import request


class ImageGalleryController(http.Controller):

    @http.route('/news_paper', type='http', auth='public', website=True)
    def image_gallery_page(self, **kwargs):
        paper = request.env['news.paper'].sudo().search([], order='date desc')
        return request.render('news-paper-gallery.news_paper_gallery_template', {
            'paper': paper
        })
