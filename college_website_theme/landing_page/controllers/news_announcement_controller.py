from odoo import http
from odoo.http import request

class HomepageNews(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def homepage_with_news(self, **kwargs):
        # Fetch original homepage content
        response = request.render('website.homepage', {})

        # Inject data if template uses extension (see next step)
        announcements = request.env['news.announcement'].sudo().search([], order='id desc')
        response.qcontext.update({
            'announcements': announcements
        })
        return response
