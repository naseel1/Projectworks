from odoo import http
from odoo.http import request
import base64

class AcademicCalendarController(http.Controller):

    @http.route(
        ['/web/content/academic-calendar/<int:rec_id>/file/<string:filename>'],
        type='http', auth='public', website=True
    )
    def custom_academic_calendar_preview(self, rec_id, filename, **kwargs):
        record = request.env['academic.calendar'].sudo().browse(rec_id)
        if not record.exists() or not record.pdf_file:
            return request.not_found()

        pdf_content = base64.b64decode(record.pdf_file)

        return request.make_response(
            pdf_content,
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'inline; filename="{filename}"'),
            ]
        )
