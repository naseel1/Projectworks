from odoo import http
from odoo.http import request


class DepartmentController(http.Controller):

    @http.route(['/programme-detail/<int:dep_id>/<string:programme_id>'], type='http', auth="public", website=True)
    def programme_detail(self, dep_id, programme_id, **kwargs):
        programme = request.env['website.department.programme'].sudo().search([
            ('programme_id', '=', programme_id),
            ('department_id.dep_id', '=', dep_id)
        ], limit=1)

        if not programme:
            return request.render("website.404")

        return request.render("landing_page.template_programme_detail", {
            'programme': programme
        })
