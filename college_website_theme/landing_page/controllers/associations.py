from odoo import http
from odoo.http import request
import re


class AssociationController(http.Controller):

    def normalize_path_to_name(self, path):
        """
        Convert 'career-guidance-placement' → 'career guidance placement'
        Remove symbols, lowercase, etc.
        """
        text = path.lower().replace('-', ' ')
        text = re.sub(r'[^a-z0-9\s]', '', text)
        return text.strip()

    @http.route(['/associations/<string:association_name>'], type='http', auth="public", website=True)
    def association_detail_page(self, association_name, **kwargs):
        clean_input = self.normalize_path_to_name(association_name)

        # Search using ilike
        association = request.env['association.manage'].sudo().search([], limit=100)
        match = False
        for rec in association:
            name = rec.association_name.lower().replace('&', '').replace('cell', '')
            name = re.sub(r'[^a-z0-9\s]', '', name)
            name = re.sub(r'\s+', ' ', name).strip()

            if name == clean_input:
                match = rec
                break

        if not match:
            return request.not_found()

        return request.render('landing_page.template_association_details', {
            'association': match,
            'reports': match.report_ids,
            'activities': match.activity_ids,
        })
