from odoo import http
from odoo.http import request


class IqacWebsiteController(http.Controller):

    @http.route(['/iqac/<string:iqac_id>/<string:name>'], type='http', auth="public", website=True)
    def iqac_item_page(self, iqac_id, name, **kwargs):
        item = request.env['iqac.main'].sudo().search([('iqac_id', '=', iqac_id)], limit=1)

        normalized_url_name = name.replace('-', ' ').lower()
        normalized_db_name = (item.name or '').lower()

        if not item or normalized_url_name != normalized_db_name:
            return request.not_found()

        return request.render("iqac_management.template_iqac_item_detail", {
            'item': item
        })

    @http.route(['/iqac-sub/<string:subitem_id>/<string:name>'], type='http', auth="public", website=True)
    def iqac_subitem_page(self, subitem_id, name, **kwargs):
        subitem = request.env['iqac.subitem'].sudo().search([('subitem_id', '=', subitem_id)], limit=1)

        normalized_url_name = name.replace('-', ' ').lower()
        normalized_db_name = (subitem.name or '').lower()

        if not subitem or normalized_url_name != normalized_db_name:
            return request.not_found()

        return request.render("iqac_management.template_iqac_item_detail", {
            'item': subitem
        })
