from odoo import http
from odoo.http import request


class ImageGalleryController(http.Controller):

    @http.route('/Home/IQAC/AQAR Documents/2175', type='http', auth='public', website=True)
    def aqar_page(self, **kwargs):
        aqar = request.env['aqar.attachment'].sudo().search([], order='date desc')
        return request.render('aqar_attachment_handler.aqar_attachment_template', {
            'aqar': aqar
        })
