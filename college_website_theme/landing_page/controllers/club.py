from odoo import http
from odoo.http import request
import base64


class ClubReportController(http.Controller):

    @http.route(['/web/content/clubreport/<int:rec_id>/file/<string:filename>'], type='http', auth='public',
                website=True)
    def custom_club_report_preview(self, rec_id, filename, **kwargs):
        report = request.env['clubs.report'].sudo().browse(rec_id)
        if not report.exists() or not report.report_file:
            return request.not_found()

        return request.make_response(
            base64.b64decode(report.report_file),
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'inline; filename="{filename}"'),
            ]
        )
