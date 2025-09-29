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

    @http.route('/api/coe-departments/<int:dep_id>/faculties', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments_faculties(self, dep_id, **kw):
        try:
            # Get confirmed API config
            api_config = request.env['embase.api_config'].sudo().search([('state', '=', 'confirm')], limit=1)
            if not api_config:
                return {'error': 'API configuration not found'}

            api_url = f"{api_config.base_url}/api/coe-departments/{dep_id}/faculties"
            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {api_config.api_token}'
            }

            r = requests.get(api_url, headers=headers, timeout=30)
            if r.status_code == 200:
                return r.json()
            else:
                return {'error': f'API Error: {r.status_code}'}

        except requests.exceptions.RequestException as e:
            return {'error': f'API Request failed: {str(e)}'}

    @http.route(['/departments/<int:dep_id>'], type='http', auth="public", website=True)
    def department_page(self, dep_id, **kwargs):
        # Fetch department from model
        department = request.env['website.department'].sudo().search([('dep_id', '=', dep_id)], limit=1)
        if not department:
            return request.render("website.404")

        # Fetch faculty data via internal method (API)
        faculty_response = self.get_departments_faculties(dep_id)
        faculties = faculty_response.get('data') if isinstance(faculty_response, dict) else []

        # Render department template
        return request.render("landing_page.template_department_detail", {
            'department': department,
            'faculties': faculties,
        })

    #  faculty profile displaying
    @http.route(['/faculty_details/<int:faculty_id>'], type='http',
                auth="public", website=True, sitemap=False)
    def faculty_profile(self, faculty_id, **kw):
        response_fac_profile = self.get_faculty_profile(faculty_id)
        response_fac_profile = json.loads(response_fac_profile)
        if response_fac_profile and 'data' in response_fac_profile:
            return request.render('mazharul_uloom_college.faculty_details_mu', {'data': response_fac_profile['data']})
        else:
            return request.render('mazharul_uloom_college.faculty_details_mu', {
                'error': 'No Data'
            })

    @http.route('/api/events/completed', methods=['GET'], type='json', auth='none', csrf=False)
    def get_home_events(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            if api_config:
                api_url = api_config.base_url + '/api/events/completed'  # Append the specific endpoint
                api_token = api_config.api_token
            else:
                return json.dumps({'error': 'API configuration not found'})

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token
            }
            r = requests.get(api_url, headers=headers, timeout=100)
            if r.status_code == 200:
                response = r.json()
            else:
                response = {'error': 'Failed to retrieve events'}

        except requests.exceptions.RequestException:
            response = {'error': 'API Request Exception'}

        return json.dumps(response)

    @http.route(['/'], type='http', auth="public", website=True, sitemap=False)
    def home_all_events(self, item_per_slide=3, items_per_slide=1, **kw):
        response_events = self.get_home_events()
        response_events = json.loads(response_events)

        # Group events into lists of three
        if 'data' in response_events:
            events_data = response_events['data']
        else:
            events_data = []

            # Group events into lists of three
        grouped_events = [events_data]

        # Group upcoming events into lists of one

        # Group upcoming events into lists of one

        return request.render('mazharul_uloom_college.mazharul_uloom_website', {
            'grouped_data': grouped_events,
        })

    @http.route('/api/events/<int:program_details_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_news_events_details(self, program_details_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/events/' + str(program_details_id)  # Append the specific endpoint
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

    @http.route(['/<int:program_details_id>/programme_detail'], type='http', auth="public",
                website=True,
                sitemap=False)
    def events_details(self, program_details_id, **kw):
        event_details = self.get_news_events_details(program_details_id)
        event_details = json.loads(event_details)

        if event_details and 'data' in event_details:
            return request.render('mazharul_uloom_college.programme_detail', {'data': event_details['data']})
        else:
            return request.render('mazharul_uloom_college.programme_detail', {
                'error': 'No Data'
            })

    @http.route('/api/events/completed', methods=['GET'], type='json', auth='none', csrf=False)
    def get_all_events(self, page=1, per_page=3, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            if api_config:
                api_url = f'{api_config.base_url}/api/events/completed'
                api_token = api_config.api_token
            else:
                return {'error': 'API configuration not found'}

            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {api_token}'
            }

            params = {
                'page': page,
                'per_page': per_page
            }

            r = requests.get(api_url, headers=headers, params=params, timeout=100)
            if r.status_code == 200:
                response = r.json()
            else:
                response = None

        except requests.exceptions.RequestException:
            response = {'error': 'API Request Exception'}

        return response

    @http.route(['/news_events'], type='http', auth="public", website=True, sitemap=False)
    def all_events(self, page=1, **kw):
        per_page = 3
        all_events = self.get_all_events(page=page, per_page=per_page)

        if all_events and 'data' in all_events:
            total_pages = all_events['meta'], ['last_page']  # Fix the typos here
            current_page = all_events['meta'], ['current_page']
            next_link = all_events['links'], ['next']
            previous_link = all_events['links'], ['prev']

            return request.render('mazharul_uloom_college.news_events', {
                'data': all_events['data'],
                'meta': all_events['meta'],
                'links': all_events['links'],
                'next_link': next_link,
                'previous_link': previous_link,
                'total_pages': total_pages,
                'current_page': current_page,
                'per_page': per_page,
            })
        else:

            return request.render('mazharul_uloom_college.news_events', {
                'error': 'No Data'
            })

    @http.route('/api/researches', methods=['GET'], type='json', auth='none', csrf=False)
    def get_research_projects(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/researches'  # Append the specific endpoint
                api_token = api_config.api_token
            else:
                return json.dumps({'error': 'API configuration not found'})

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token,
            }
            r = requests.get(api_url, headers=headers, timeout=100)
            if r.status_code == 200:
                response = r.json()
            else:
                response = {'error': f'API returned status code {r.status_code}'}

        except requests.exceptions.RequestException as e:
            response = {'error': f'API Request Exception: {str(e)}'}

        return json.dumps(response)

    @http.route(['/projects'], type='http', auth="public", website=True, sitemap=False)
    def research_projects(self, **kw):
        research_projects = self.get_research_projects()
        research_projects = json.loads(research_projects)
        if 'data' in research_projects and 'data' in research_projects:
            return request.render('website.projects', {'data': research_projects['data']})
        else:
            return request.render('website.projects', {
                'error': research_projects.get('error', 'No Data')
            })

    @http.route('/api/publications/', methods=['GET'], type='json', auth='none', csrf=False)
    def get_research_publications(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].sudo().search([('state', '=', 'confirm')], limit=1)

            if not api_config:
                _logger.error("BooksAuthored: API configuration not found")
                return {'error': 'API configuration not found'}

            api_url = api_config.base_url.rstrip('/') + '/api/publications'
            api_token = api_config.api_token

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token,
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

    @http.route('/api/booksAuthored', methods=['GET'], type='json', auth='none', csrf=False)
    def get_research_publications_books(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].sudo().search([('state', '=', 'confirm')], limit=1)

            if not api_config:
                _logger.error("BooksAuthored: API configuration not found")
                return {'error': 'API configuration not found'}

            api_url = api_config.base_url.rstrip('/') + '/api/booksAuthored'
            api_token = api_config.api_token

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token,
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

    @http.route(['/publications'], type='http', auth="public", website=True, sitemap=False)
    def research_publication(self, **kw):
        journals_proceedings = self.get_research_publications()
        books = self.get_research_publications_books()

        # Convert JSON string to dict if needed
        if isinstance(journals_proceedings, str):
            journals_proceedings = json.loads(journals_proceedings)
        if isinstance(books, str):
            books = json.loads(books)

        if journals_proceedings and books and \
                'journals' in journals_proceedings and \
                'proceedings' in journals_proceedings and \
                'data' in books:
            return request.render('website.publications', {
                'data': journals_proceedings['journals'],
                'data2': journals_proceedings['proceedings'],
                'books': books['data']
            })
        else:
            return request.render('website.publications', {
                'error': 'No Data'
            })
