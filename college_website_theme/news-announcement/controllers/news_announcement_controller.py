from odoo import http
from odoo.http import request


class HomepageNews(http.Controller):

    @http.route('/', type='http', auth='public', website=True, sitemap=False)
    def homepage_with_news(self, **kwargs):
        # Fetch original homepage content

        # Inject data if template uses extension (see next step)
        announcements = request.env['news.announcement'].sudo().search([], order='id desc')
        return request.render('website.homepage', {
            'announcements': announcements
        })
