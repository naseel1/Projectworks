from odoo import http
from odoo.http import request


class DepController(http.Controller):

    @http.route(['/departments/<int:dep_id>'], type='http', auth="public", website=True)
    def department_page(self, dep_id, **kwargs):
        department = request.env['website.department'].sudo().search([('dep_id', '=', dep_id)], limit=1)

        if not department:
            return request.render("website.404")

        return request.render("landing_page.template_department_detail", {
            'department': department
        })
