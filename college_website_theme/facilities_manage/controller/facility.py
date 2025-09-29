from odoo import http
from odoo.http import request
import re


class FacilitiesWebsiteController(http.Controller):

    def normalize_path_to_name(self, path):
        # Normalize like your original controller: slug → name
        text = path.lower()
        text = text.replace('-', ' ')
        text = text.replace('/', ' ')
        text = text.replace('&', ' and ')
        text = re.sub(r'[^a-z0-9\s]', '', text)
        return re.sub(r'\s+', ' ', text).strip()

    @http.route(['/facility/<string:facility_name>'], type='http', auth="public", website=True)
    def facility_detail_page(self, facility_name, **kwargs):
        clean_input = self.normalize_path_to_name(facility_name)

        facilities = request.env['facility.manage'].sudo().search([])
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

        return request.render('facilities_manage.template_facility_page', {
            'facility': match
        })
