from odoo import http
from odoo.http import request
import re


class FacilitiesController(http.Controller):

    def normalize_path_to_name(self, path):
        # Normalize slugs like 'auditorium-conference-halls' → 'auditorium conference halls'
        text = path.lower()
        text = text.replace('-', ' ')  # Convert dashes to space
        text = text.replace('/', ' ')  # Replace slashes with space
        text = text.replace('&', ' and ')  # Replace & with 'and'
        text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove other symbols
        return re.sub(r'\s+', ' ', text).strip()

    @http.route(['/facilities/<string:facility_name>'], type='http', auth="public", website=True)
    def facility_detail_page(self, facility_name, **kwargs):
        clean_input = self.normalize_path_to_name(facility_name)

        facilities = request.env['facilities.manage'].sudo().search([])
        match = False
        for rec in facilities:
            name = rec.name.lower()
            name = name.replace('&', ' and ')
            name = name.replace('/', ' ')
            name = re.sub(r'[^a-z0-9\s]', '', name)
            name = re.sub(r'\s+', ' ', name).strip()

            if name == clean_input:
                match = rec
                break

        if not match:
            return request.not_found()

        return request.render('landing_page.template_facility_details', {
            'facility': match,
            'sub_facilities': match.child_ids,
        })
