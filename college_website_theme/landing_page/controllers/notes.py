from odoo import http
from odoo.http import request
from collections import defaultdict


class DepartmentController(http.Controller):

    # STEP 1: Show all departments — this can be handled directly in QWeb using t-foreach,
    # so no controller needed for /notes.

    # STEP 2: Show all semesters for a selected department
    @http.route(['/notes/<string:notes_title>'], type='http', auth="public", website=True)
    def department_page(self, notes_title, **kwargs):
        # Convert 'BCA-Science' back to 'BCA Science'
        clean_title = notes_title.replace('-', ' ')

        department = request.env['notes.update'].sudo().search([
            ('notes_title', '=', clean_title)
        ], limit=1)

        if not department:
            return request.render("landing_page.custom_404_template")  # Avoid using website.404

        semesters = [
            {'key': 'semester1_ids', 'number': 1, 'label': '1 Semester'},
            {'key': 'semester2_ids', 'number': 2, 'label': '2 Semester'},
            {'key': 'semester3_ids', 'number': 3, 'label': '3 Semester'},
            {'key': 'semester4_ids', 'number': 4, 'label': '4 Semester'},
            {'key': 'semester5_ids', 'number': 5, 'label': '5 Semester'},
            {'key': 'semester6_ids', 'number': 6, 'label': '6 Semester'},
        ]

        valid_semesters = []
        for sem in semesters:
            semester_records = getattr(department, sem['key'], False)
            if semester_records and len(semester_records) > 0:
                valid_semesters.append(sem)

        return request.render("landing_page.template_notes_detail", {
            'notes_title': department.notes_title,
            'semesters': valid_semesters,
        })

    # STEP 3: Show files under specific department and semester
    @http.route(['/notes/<string:notes_title>/<int:semester_num>'], type='http', auth="public", website=True)
    def semester_detail_page(self, notes_title, semester_num, **kwargs):
        if semester_num not in range(1, 7):
            return request.render("landing_page.custom_404_template")

        # Convert dash back to space
        clean_title = notes_title.replace('-', ' ')
        semester_key = f'semester{semester_num}_ids'

        department = request.env['notes.update'].sudo().search([('notes_title', '=', clean_title)], limit=1)
        if not department or not hasattr(department, semester_key):
            return request.render("landing_page.custom_404_template")

        files = getattr(department, semester_key)

        return request.render("landing_page.template_notes_semester_detail", {
            'notes_title': clean_title,
            'semester_number': semester_num,
            'files': files,
        })
