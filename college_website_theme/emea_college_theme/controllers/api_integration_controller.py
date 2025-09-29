from odoo import http
from odoo.http import request
import requests
import json


class EmbaseApiController(http.Controller):

    @http.route('/your-endpoint', methods=['POST'], type='json', auth='none', csrf=False)
    def api_controller(self, **kw):
        try:

            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url
                api_token = api_config.api_token
            else:
                return {'error': 'API configuration not found'}

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token
            }
            r = requests.get(api_url, headers=headers, timeout=10)
            if r.status_code == 200:
                response = r.json()
            else:
                response = None

        except requests.exceptions.RequestException:
            response = {'error': 'API Request Exception'}

        json_data = json.dumps(response)
        return json_data

    # faculty profile endpoint
    @http.route('/api/faculties/<int:faculty_id>/profile', methods=['GET'], type='json', auth='none', csrf=False)
    def get_faculty_profile(self, faculty_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/faculties/' + str(
                    faculty_id) + '/profile'  # Append the specific endpoint
                api_token = api_config.api_token
            else:
                return {'error': 'API configuration not found'}

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token
            }
            r = requests.get(api_url, headers=headers, timeout=100)
            if r.status_code == 200:
                response = r.json()
            else:
                response = None

        except requests.exceptions.RequestException:
            response = {'error': 'API Request Exception'}

        json_data = json.dumps(response)
        return json_data

    #  faculty profile displaying
    @http.route(['/staffdetails/<int:faculty_id>'], type='http',
                auth="public", website=True, sitemap=False)
    def faculty_profile(self, faculty_id, **kw):
        response_fac_profile = self.get_faculty_profile(faculty_id)
        response_fac_profile = json.loads(response_fac_profile)
        if response_fac_profile and 'data' in response_fac_profile:
            return request.render('emea_college_theme.staffdetails_emea', {'data': response_fac_profile['data']})
        else:
            return request.render('emea_college_theme.staffdetails_emea', {
                'error': 'No Data'
            })





