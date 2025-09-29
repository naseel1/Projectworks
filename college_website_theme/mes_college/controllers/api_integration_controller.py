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

    # All Departments endpoint
    @http.route('/api/coe-departments', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/coe-departments'  # Append the specific endpoint
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
                response = {'error': f'API returned status code {r.status_code}'}

        except requests.exceptions.RequestException as e:
            response = {'error': f'API Request Exception: {str(e)}'}

        json_data = json.dumps(response)
        return json_data

    # list all departments
    @http.route(['/departments'], type='http', auth="public", website=True, sitemap=False)
    def get_department(self, **kw):
        response_dict = self.get_departments()
        response_dict = json.loads(response_dict)

        if response_dict and 'departments' in response_dict and 'allied_departments' in response_dict:
            return request.render('mes_college.departments_mes', {
                'departments': response_dict['departments'],
                'allied_departments': response_dict['allied_departments']
            })

        else:
            # Handle the error, e.g., render an error page or return a default value
            return request.render('mes_college.departments_mes', {
                'error': 'No Data'
            })

    dep_id = []
    program_details_id = []

    @http.route('/api/coe-departments/<int:dep_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments_pages(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/coe-departments/' + str(dep_id)  # Append the specific endpoint
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

    # single department page displaying
    @http.route(['/department/<int:dep_id>'], type='http', auth="public", website=True, sitemap=False)
    def get_department_page(self, dep_id, **kw):
        print(dep_id)
        response_page = self.get_departments_pages(dep_id)

        try:
            response_page = json.loads(response_page)
            data = response_page.get('data', None)

            if data:
                return request.render('mes_college.department_page_mes', {'data': data})
            else:
                # No data in response_page, render a plain error page
                return request.render('mes_college.department_page_mes',
                                      {'error_message': 'No data available for department ID {}'.format(dep_id)})

        except json.JSONDecodeError as e:
            # Handle JSON decoding error, render an error page
            return request.render('mes_college.department_page_mes',
                                  {'error_message': 'Error decoding JSON: {}'.format(str(e))})

    # department faculty endpoint
    @http.route('/api/coe-departments/<int:dep_id>/faculties', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments_faculties(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/coe-departments/' + str(dep_id) + '/faculties'
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

    # department faculty displaying
    @http.route(['/department/<int:dep_id>/faculty'], type='http', auth="public", website=True,
                sitemap=False)
    def get_faculties(self, dep_id, **kw):
        response_fac = self.get_departments_faculties(dep_id)
        response_fac = json.loads(response_fac)
        return request.render('mes_college.department_faculties_mes', {'data': response_fac['data']})

        # return request.render('website.page_404', {})

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
    @http.route(['/department/<int:dep_id>/faculty/<int:faculty_id>/profile'], type='http',
                auth="public", website=True, sitemap=False)
    def faculty_profile(self, faculty_id, **kw):
        response_fac_profile = self.get_faculty_profile(faculty_id)
        response_fac_profile = json.loads(response_fac_profile)
        return request.render('mes_college.faculty_profile_mes', {'data': response_fac_profile['data']})

    # department Reports Endpoint
    @http.route('/api/coe-departments/<int:dep_id>/reports', methods=['GET'], type='json', auth='none', csrf=False)
    def get_department_reports(self, dep_id, page=1, per_page=12, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            if api_config:
                api_url = f"{api_config.base_url}/api/coe-departments/{dep_id}/reports"
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
            response = requests.get(api_url, headers=headers, params=params, timeout=100)

            if response.status_code == 200:
                return response.json()
            else:
                return {'error': f"API Request failed with status code {response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {'error': f"API Request Exception: {str(e)}"}


    @http.route(['/department/<int:dep_id>/department_reports'], type='http', auth='public', website=True,
                sitemap=False)
    def departments_reports(self, dep_id, page=1, **kw):
        response_department_reports = self.get_departments_pages(dep_id)
        response_department_reports = json.loads(response_department_reports)

        data_to_render = {'data': response_department_reports.get('data', [])}

        per_page = 3
        department_reports = self.get_department_reports(dep_id, page=page, per_page=per_page)

        if department_reports and 'data' in department_reports:
            meta = department_reports.get('meta', {})
            links = department_reports.get('links', {})

            data_to_render.update({
                'depart_data': department_reports['data'],
                'meta': meta,
                'links': links,
                'next_link': links.get('next'),
                'previous_link': links.get('prev'),
                'total_page': meta.get('last_page', 1),
                'current_page': meta.get('current_page', 1),
                'per_page': per_page
            })

        return request.render('mes_college.department_reports_mes', data_to_render)

    # department gallery Endpoint
    @http.route('/api/departments/<int:dep_id>/gallery', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments_gallery(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/departments/' + str(dep_id) + '/gallery'
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

    # department gallery displaying
    @http.route(['/department/<int:dep_id>/dep_gallery'], type='http', auth="public", website=True, sitemap=False)
    def departments_gallery(self, dep_id, **kw):
        response_galleries = self.get_departments_gallery(dep_id)
        response_galleries = json.loads(response_galleries)

        response_gallery = self.get_departments_pages(dep_id)
        response_gallery = json.loads(response_gallery)

        return request.render('mes_college.department_gallery', {
            'depart_data': response_galleries['data'], 'data': response_gallery['data']})

    #  Principal profile endpoint
    @http.route('/api/academic-heads/principalProfile', methods=['GET'], type='json', auth='none', csrf=False)
    def get_principal_profile(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/academic-heads/principalProfile'  # Append the specific endpoint
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

    #  Principal profile displaying
    @http.route(['/principal_profile'], type='http', auth="public", website=True, sitemap=False)
    def principal_profile(self, **kw):
        response_principal = self.get_principal_profile()
        response_principal = json.loads(response_principal)
        return request.render('mes_college.principal_profile_mes', {'data': response_principal['data']})

        # return request.render('website.page_404', {})

        # programmes endpoint

    @http.route('/api/programmes/', methods=['GET'], type='json', auth='none', csrf=False)
    def get_programmes(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/programmes'  # Append the specific endpoint
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

    @http.route(['/programmes'], type='http', auth="public", website=True, sitemap=False)
    def programme(self, **kw):
        response_prog = self.get_programmes()
        response_prog = json.loads(response_prog)
        if response_prog and 'data' in response_prog:
            return request.render('mes_college.programmes_mes', {'data': response_prog['data']})
        else:
            return request.render('mes_college.programmes_mes', {
                'error': 'No Data'
            })

    @http.route('/api/programmes?dep_id=<int:dep_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_depart_programmes(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/programmes?dep_id=' + str(dep_id)  # Append the specific endpoint
                api_token = api_config.api_token
            else:
                return {'error': 'API configuration not found'}

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token,
                'dep_id': '[]'
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

    @http.route(['/department/<int:dep_id>/programme'], type='http', auth="public", website=True, sitemap=False)
    def department_programme(self, dep_id, **kw):
        response_programme = self.get_depart_programmes(dep_id)
        response_programme = json.loads(response_programme)

        response_depart_programme = self.get_departments_pages(dep_id)
        response_depart_programme = json.loads(response_depart_programme)
        return request.render('mes_college.department_programmes_mes', {
            'programme_data': response_programme['data'],
            'data': response_depart_programme['data']
        })

    @http.route('/api/coe-departments/<int:dep_id>/events', methods=['GET'], type='json', auth='none', csrf=False)
    def get_department_events(self, dep_id, page=1, per_page=12, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            if api_config:
                api_url = f"{api_config.base_url}/api/coe-departments/{dep_id}/events"  # Append the specific endpoint
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
            response = requests.get(api_url, headers=headers, params=params, timeout=100)
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': f"API Request failed with status code {response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {'error': f"API Request Exception: {str(e)}"}

    @http.route(['/department/<int:dep_id>/activities'], type='http', auth="public", website=True, sitemap=False)
    def departments_events(self, dep_id, page=1, **kw):
        response_depart_events = self.get_departments_pages(dep_id)
        response_depart_events = json.loads(response_depart_events)
        data_to_render = {
            'data': response_depart_events['data'],
        }
        per_page = 3
        department_events = self.get_department_events(dep_id, page=page, per_page=per_page)
        if department_events and 'data' in department_events:
            total_page = department_events['meta'], ['last_page']
            current_page = department_events['meta'], ['current_page']
            next_link = department_events['links'], ['next']
            previous_link = department_events['links'], ['prev']
            data_to_render.update({
                'event': department_events['data'],
                'meta': department_events['meta'],
                'links': department_events['links'],
                'next_link': next_link,
                'previous_link': previous_link,
                'total_page': total_page,
                'current_page': current_page,
                'per_page': per_page
            })
        return request.render('mes_college.department_activities', data_to_render)

    @http.route('/api/events/<int:program_details_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_department_events_details(self, program_details_id, **kw):
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

    @http.route(['/department/<int:dep_id>/<int:program_details_id>/activitydetails'], type='http', auth="public",
                website=True,
                sitemap=False)
    def activity_details(self, program_details_id, **kw):

        departments_activity_detail = self.get_department_events_details(program_details_id)
        departments_activity_detail = json.loads(departments_activity_detail)

        return request.render('mes_college.activities_detail', {'data': departments_activity_detail['data']})

    @http.route('/api/facilities?dep_id=<int:dep_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_depart_facilities(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/facilities?dep_id=' + str(dep_id)  # Append the specific endpoint
                api_token = api_config.api_token
            else:
                return {'error': 'API configuration not found'}

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token,
                'dep_id': '[]'
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

    @http.route(['/department/<int:dep_id>/facilities'], type='http', auth="public", website=True,
                sitemap=False)
    def department_facilities(self, dep_id, **kw):
        response_facilities = self.get_depart_facilities(dep_id)
        response_facilities = json.loads(response_facilities)

        response_department_facility = self.get_departments_pages(dep_id)
        response_department_facility = json.loads(response_department_facility)
        if response_facilities and 'data' in response_facilities:
            return request.render('mes_college.department_facilities', {
                'facility_data': response_facilities['data'],
                'data': response_department_facility['data']
            })
        else:
            return request.render('mes_college.department_facilities', {
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

    @http.route(['/research-projects'], type='http', auth="public", website=True, sitemap=False)
    def research_projects(self, **kw):
        research_projects = self.get_research_projects()
        research_projects = json.loads(research_projects)
        if 'data' in research_projects and 'data' in research_projects:
            return request.render('mes_college.research-projects', {'data': research_projects['data']})
        else:
            return request.render('mes_college.research-projects', {
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

    @http.route(['/research-publications_faculty'], type='http', auth="public", website=True, sitemap=False)
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
            return request.render('mes_college.research-publications_faculty', {
                'data': journals_proceedings['journals'],
                'data2': journals_proceedings['proceedings'],
                'books': books['data']
            })
        else:
            return request.render('mes_college.research-publications_faculty', {
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

            return request.render('mes_college.news_events', {
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

            return request.render('mes_college.news_events', {
                'error': 'No Data'
            })

    # @http.route(['/seminars-workshops'], type='http', auth="public", website=True, sitemap=False)
    # def seminars(self, page=1, **kw):
    #     per_page = 3
    #     seminars_workshops = self.get_all_events(page=page, per_page=per_page)
    #
    #     if seminars_workshops and 'data' in seminars_workshops:
    #         total_pages = seminars_workshops['meta'], ['last_page']  # Fix the typos here
    #         current_page = seminars_workshops['meta'], ['current_page']
    #         next_link = seminars_workshops['links'], ['next']
    #         previous_link = seminars_workshops['links'], ['prev']
    #
    #         return request.render('mes_college.seminars-workshops', {
    #             'data': seminars_workshops['data'],
    #             'meta': seminars_workshops['meta'],
    #             'links': seminars_workshops['links'],
    #             'next_link': next_link,
    #             'previous_link': previous_link,
    #             'total_pages': total_pages,
    #             'current_page': current_page,
    #             'per_page': per_page,
    #         })
    #
    #     return {'error': 'Unable to fetch events'}

    @http.route('/api/events?is_research=true', methods=['GET'], type='json', auth='none', csrf=False)
    def get_seminars(self, page=1, per_page=3, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            if api_config:
                api_url = api_config.base_url + '/api/events?is_research=true'
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

    @http.route(['/seminars-workshops'], type='http', auth="public", website=True, sitemap=False)
    def all_seminar(self, page=1, **kw):
        per_page = 3
        all_seminar = self.get_seminars(page=page, per_page=per_page)

        if all_seminar and 'data' in all_seminar:
            total_pages = all_seminar['meta'], ['last_page']  # Fix the typos here
            current_page = all_seminar['meta'], ['current_page']
            next_link = all_seminar['links'], ['next']
            previous_link = all_seminar['links'], ['prev']

            return request.render('mes_college.seminars-workshops', {
                'data': all_seminar['data'],
                'meta': all_seminar['meta'],
                'links': all_seminar['links'],
                'next_link': next_link,
                'previous_link': previous_link,
                'total_pages': total_pages,
                'current_page': current_page,
                'per_page': per_page,
            })

        return request.render('mes_college.seminars-workshops', {
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

        return request.render('mes_college.mes_college_home', {
            'grouped_data': grouped_events,
            'item_per_slide': item_per_slide,
            'grouped_upcoming_data': grouped_upcoming_events,
            'items_per_slide': items_per_slide,
        })

    @http.route(['/home'], type='http', auth="public", website=True, sitemap=False)
    def homepage_all_events(self, item_per_slide=3, items_per_slide=1, **kw):
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

        return request.render('mes_college.mes_college_home', {
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

    @http.route(['/<int:program_details_id>/programme_detail'], type='http', auth="public",
                website=True,
                sitemap=False)
    def events_details(self, program_details_id, **kw):
        event_details = self.get_news_events_details(program_details_id)
        event_details = json.loads(event_details)

        if event_details and 'data' in event_details:
            return request.render('mes_college.programme_detail', {'data': event_details['data']})
        else:
            return request.render('mes_college.programme_detail', {
                'error': 'No Data'
            })

    @http.route(['/upcoming/<int:program_details_id>'], type='http', auth="public",
                website=True,
                sitemap=False)
    def upcoming_events_details(self, program_details_id, **kw):
        upcoming_events_details = self.get_news_events_details(program_details_id)
        upcoming_events_details = json.loads(upcoming_events_details)

        if upcoming_events_details and 'data' in upcoming_events_details:
            return request.render('mes_college.upcoming_activity_detail', {'data': upcoming_events_details['data']})
        else:
            return request.render('mes_college.upcoming_activity_detail', {
                'error': 'No Data'
            })

    @http.route(['/news/<int:program_details_id>/news_detail'], type='http', auth="public",
                website=True,
                sitemap=False)
    def all_events_details(self, program_details_id, **kw):
        all_event_details = self.get_news_events_details(program_details_id)
        all_event_details = json.loads(all_event_details)

        return request.render('mes_college.news_detail', {'data': all_event_details['data']})

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

    @http.route(['/clubs', ], type='http', auth="public", website=True, sitemap=False)
    def clubs_page(self, **kw):
        # Fetch list of clubs
        clubs_response = self.get_clubs()
        clubs_data = json.loads(clubs_response)

        club_detail_data = {}
        if clubs_data and 'data' in clubs_data:
            first_club_id = clubs_data['data'][0].get('club_id')
            if first_club_id:
                club_detail_response = self.get_clubs_detail(first_club_id)
                club_detail_data = json.loads(club_detail_response).get('data', {})

        return request.render('mes_college.clubs', {
            'data': clubs_data.get('data', []),
            'detail': club_detail_data
        })

    @http.route(['/clubs/<int:club_id>'], type='http', auth="public", website=True, sitemap=False)
    def clubs(self, club_id, **kw):
        try:
            response_club_detail = self.get_clubs()
            response_club_detail = json.loads(response_club_detail)

            response_club_details = self.get_clubs_detail(club_id)
            response_clubs_details = json.loads(response_club_details)

            print("response_club_detail:", response_club_detail)
            print("response_clubs_details:", response_clubs_details)

            if 'data' in response_club_detail and 'data' in response_clubs_details:
                return request.render('mes_college.clubs_detail',
                                      {'data': response_club_detail['data'], 'detail': response_clubs_details['data']})
            else:
                return request.render('mes_college.clubs_detail', {
                    'error': response_clubs_details.get('error', 'No Data')
                })

        except Exception as e:
            return json.dumps({'error': str(e)})

    @http.route('/api/facilities?research_facility=1', methods=['GET'], type='json', auth='none', csrf=False)
    def get_facilities(self, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/facilities?research_facility=1'  # Append the specific endpoint
                api_token = api_config.api_token
            else:
                return {'error': 'API configuration not found'}

            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' % api_token,
                'dep_id': '[]'
            }
            r = requests.get(api_url, headers=headers, timeout=100)
            r.raise_for_status()  # Raise an HTTPError for any bad status code
            response = r.json()

        except requests.exceptions.RequestException as e:
            response = {'error': 'API Request Exception: {}'.format(str(e))}

        return json.dumps(response)

    @http.route(['/res-facilities'], type='http', auth="public", website=True, sitemap=False)
    def research_facilities(self, **kw):
        response_research_facilities = self.get_facilities()

        response_research_facilities = json.loads(response_research_facilities)
        if 'data' in response_research_facilities and 'data' in response_research_facilities:

            return request.render('mes_college.res-facilities', {'data': response_research_facilities['data']})

        else:
            return request.render('mes_college.res-facilities', {
                'error': response_research_facilities.get('error', 'No Data')
            })

    @http.route('/api/researches?dep_id=<int:dep_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_department_projects(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/researches?dep_id=' + str(dep_id)  # Append the specific endpoint
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

    @http.route(['/department/<int:dep_id>/projects'], type='http', auth="public", website=True, sitemap=False)
    def departments_projects(self, dep_id, **kw):
        departments_projects = self.get_department_projects(dep_id)
        departments_projects = json.loads(departments_projects)

        response_project_dep = self.get_departments_pages(dep_id)
        response_project_dep = json.loads(response_project_dep)

        return request.render('mes_college.department_projects', {
            'depart_project': departments_projects['data'], 'data': response_project_dep['data']})

    @http.route('/api/coe-departments/<int:dep_id>/batches', methods=['GET'], type='json', auth='none', csrf=False)
    def get_departments_exam_results(self, dep_id, **kw):
        try:
            # Retrieve API configuration record
            api_config = request.env['embase.api_config'].search([('state', '=', 'confirm')], limit=1)
            print("api_config", api_config)
            if api_config:
                api_url = api_config.base_url + '/api/coe-departments/' + str(dep_id) + '/batches'
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

    # department exam results displaying
    @http.route(['/department/<int:dep_id>/exam_results'], type='http', auth="public", website=True, sitemap=False)
    def departments_exam_results(self, dep_id, **kw):
        response_exam_results = self.get_departments_exam_results(dep_id)
        response_exam_results = json.loads(response_exam_results)

        response_depart_exam_results = self.get_departments_pages(dep_id)
        response_depart_exam_results = json.loads(response_depart_exam_results)

        return request.render('mes_college.department_exam_results', {
            'exam_result': response_exam_results['data'], 'data': response_depart_exam_results['data']})

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
        return request.render('mes_college.exam_results_view', {
            'internal': response_exam_results['data'], 'internal_paper': response_exam_results['papers']})
