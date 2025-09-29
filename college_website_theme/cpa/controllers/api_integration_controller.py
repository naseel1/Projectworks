from odoo import http
from odoo.http import request, _logger
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

    @http.route('/api/coe-departments/<int:dep_id>/batches', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments_exam_results(self, dep_id, **kw):
        try:
            api_config = request.env['embase.api_config'].sudo().search([('state', '=', 'confirm')], limit=1)
            if not api_config:
                _logger.error("API config not found")
                return {'error': 'API configuration not found'}

            api_url = f"{api_config.base_url}/api/coe-departments/{dep_id}/batches"
            api_token = api_config.api_token

            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {api_token}'
            }

            _logger.info(f"[API CALL] GET {api_url}")
            r = requests.get(api_url, headers=headers, timeout=100)

            if r.status_code == 200:
                _logger.info("API response OK")
                return r.json()
            else:
                _logger.error(f"API error {r.status_code}: {r.text}")
                return {'error': f'API Error: {r.status_code}', 'details': r.text}

        except requests.exceptions.RequestException as e:
            _logger.exception("API request exception")
            return {'error': f'API Request Exception: {str(e)}'}

    @http.route(['/departments/<int:dep_id>'], type='http', auth="public", website=True)
    def department_page(self, dep_id, **kwargs):
        department = request.env['website.department'].sudo().search([('dep_id', '=', dep_id)], limit=1)
        if not department:
            return request.render("website.404")

        # Faculties
        faculty_response = self.get_departments_faculties(dep_id)
        faculties = faculty_response.get('data') if isinstance(faculty_response, dict) else []

        # ✅ FIX: Ensure we extract batches properly
        batch_response = self.get_departments_exam_results(dep_id)
        batches = batch_response.get('data') if isinstance(batch_response, dict) else []

        return request.render("landing_page.template_department_detail", {
            'department': department,
            'faculties': faculties,
            'batches': batches,
        })

    #  faculty profile displaying
    @http.route(['/faculty_details/<int:faculty_id>'], type='http',
                auth="public", website=True, sitemap=False)
    def faculty_profile(self, faculty_id, **kw):
        response_fac_profile = self.get_faculty_profile(faculty_id)
        response_fac_profile = json.loads(response_fac_profile)
        if response_fac_profile and 'data' in response_fac_profile:
            return request.render('cpa.faculty_details_cpa', {'data': response_fac_profile['data']})
        else:
            return request.render('cpa.faculty_details_cpa', {
                'error': 'No Data'
            })

    @http.route('/api/events/upcoming', methods=['GET'], type='json', auth='none', csrf=False)
    def get_upcoming_events(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            if api_config:
                api_url = api_config.base_url + '/api/events/upcoming'  # Append the specific endpoint
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

    @http.route(['/home'], type='http', auth="public", website=True, sitemap=False)
    def home_all_events(self, item_per_slide=3, items_per_slide=1, **kw):
        response_events = self.get_home_events()
        response_events = json.loads(response_events)

        # Group events into lists of three
        if 'data' in response_events:
            events_data = response_events['data']
        else:
            events_data = []

            # Group events into lists of three
        grouped_events = [events_data[i:i + item_per_slide] for i in range(0, len(events_data), item_per_slide)]

        response_upcoming_event = self.get_upcoming_events()
        response_upcoming_events = json.loads(response_upcoming_event)

        # Group upcoming events into lists of one
        if 'data' in response_upcoming_events:
            upcoming_events_data = response_upcoming_events['data']
        else:
            upcoming_events_data = []

            # Group upcoming events into lists of one
        grouped_upcoming_events = [upcoming_events_data[i:i + items_per_slide] for i in
                                   range(0, len(upcoming_events_data), items_per_slide)]

        return request.render('website.home', {
            'grouped_data': grouped_events,
            'item_per_slide': item_per_slide,
            'grouped_upcoming_data': grouped_upcoming_events,
            'items_per_slide': items_per_slide,
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

    @http.route(['/<int:program_details_id>/event_details'], type='http', auth="public",
                website=True,
                sitemap=False)
    def events_details(self, program_details_id, **kw):
        event_details = self.get_news_events_details(program_details_id)
        event_details = json.loads(event_details)

        if event_details and 'data' in event_details:
            return request.render('cpa.event_detail', {'data': event_details['data']})
        else:
            return request.render('cpa.event_detail', {
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

    @http.route(['/events'], type='http', auth="public", website=True, sitemap=False)
    def all_events(self, page=1, **kw):
        per_page = 3
        all_events = self.get_all_events(page=page, per_page=per_page)

        if all_events and 'data' in all_events:
            total_pages = all_events['meta'], ['last_page']  # Fix the typos here
            current_page = all_events['meta'], ['current_page']
            next_link = all_events['links'], ['next']
            previous_link = all_events['links'], ['prev']

            return request.render('cpa.events', {
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

            return request.render('cpa.events', {
                'error': 'No Data'
            })

    @http.route('/api/batches/<int:batch_id>/semester/<int:term>/internals', methods=['GET'], type='json', auth='none',
                csrf=False)
    def get_exam_results_view(self, batch_id, term, **kw):
        try:
            # Retrieve API configuration record

            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)

            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/batches/' + str(batch_id) + '/semester/' + str(
                    term) + '/internals'
                # Append the specific endpoint
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

    @http.route(['/batches/<int:batch_id>/semester/<int:term>/internals'], type='http', auth="public",
                website=True,
                sitemap=False)
    def exam_results_view(self, batch_id, term, **kw):
        response_exam_results_view = self.get_exam_results_view(batch_id, term)
        response_exam_results = json.loads(response_exam_results_view)
        print(response_exam_results['data'])
        print(term)
        return request.render('cpa.exam_results_view', {
            'internal': response_exam_results['data'], 'internal_paper': response_exam_results['papers']})

    @http.route('/api/clubs/', methods=['GET'], type='json', auth='none', csrf=False)
    def get_clubs(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/clubs'  # Append the specific endpoint
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

    # clubs details
    @http.route('/api/clubs/<int:club_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_clubs_detail(self, club_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/clubs/' + str(club_id)  # Append the specific endpoint
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

    @http.route(['/clubs/<string:club_name>'], type='http', auth="public", website=True)
    def club_detail_page(self, club_name, **kwargs):
        try:
            clean_name = club_name.replace('-', ' ').strip().lower()

            # Step 1: Always load local model record
            club = request.env['clubs.manage'].sudo().search([
                ('club_name', 'ilike', clean_name)
            ], limit=1)
            if not club:
                return request.not_found()

            # Step 2: Try to fetch API club list (optional)
            club_list = []
            api_club_id = None
            try:
                response_club_list = self.get_clubs()
                club_list_data = json.loads(response_club_list) if response_club_list else {}
                club_list = club_list_data.get('data', [])

                # Match API club by name
                api_club = next(
                    (c for c in club_list if c.get('club_name', '').strip().lower() == clean_name),
                    None
                )
                api_club_id = api_club.get('club_id') if api_club else None

            except Exception:
                pass  # Fail silently — club_list stays empty

            # Step 3: Try to get club_detail from API using club_id
            club_detail = {}
            if api_club_id:
                try:
                    response_club_detail = self.get_clubs_detail(api_club_id)
                    club_detail_data = json.loads(response_club_detail) if response_club_detail else {}
                    club_detail = club_detail_data.get('data', {})
                except Exception:
                    pass  # Fail silently — club_detail stays empty

            # Step 4: Render with or without club_detail
            return request.render("landing_page.template_club_details", {
                'club': club,
                'club_list': club_list,
                'club_detail': club_detail,
            })

        except Exception as e:
            return request.render("landing_page.template_club_details", {
                'club': False,
                'error': str(e)
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
            return request.render('cpa.programme_detail', {'data': event_details['data']})
        else:
            return request.render('cpa.programme_detail', {
                'error': 'No Data'
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

    @http.route('/api/researches', methods=['GET'], type='json', auth='none', csrf=False)
    def get_research_projects(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].sudo().search([('state', '=', 'confirm')], limit=1)

            if not api_config:
                _logger.error("BooksAuthored: API configuration not found")
                return {'error': 'API configuration not found'}

            api_url = api_config.base_url.rstrip('/') + '/api/researches'
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

    @http.route(['/research-publications'], type='http', auth="public", website=True, sitemap=False)
    def research_publication(self, **kw):
        journals_proceedings = self.get_research_publications()
        books = self.get_research_publications_books()
        researches = self.get_research_projects()

        # Convert JSON string to dict if needed
        if isinstance(journals_proceedings, str):
            journals_proceedings = json.loads(journals_proceedings)
        if isinstance(books, str):
            books = json.loads(books)
        if isinstance(researches, str):
            researches = json.loads(researches)

        # ✅ use the same safe check as in research_projects
        if journals_proceedings and books and researches and \
                'journals' in journals_proceedings and \
                'proceedings' in journals_proceedings and \
                'data' in books and \
                'data' in researches:
            return request.render('website.research-publications', {
                'data': journals_proceedings['journals'],
                'data2': journals_proceedings['proceedings'],
                'books': books['data'],
                'researches': researches['data'],  # ✅ consistent with your working code
            })
        else:
            return request.render('website.research-publications', {
                'error': 'No Data'
            })
