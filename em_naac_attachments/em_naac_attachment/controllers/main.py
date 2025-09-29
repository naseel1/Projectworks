# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2023 Emdot Mincetech Pvt. Ltd (<https://www.mincetech.com>). All Rights Reserved.
#       Developer : Nikhil Krishnan
#
##############################################################################################

from odoo import http
from odoo.http import request


class WebsiteBusinessProceduresController(http.Controller):

    @http.route(['/naac/<string:category>/<string:subcategory>/<string:handler>',
                 '/naac/<string:category>/<string:subcategory>/<string:handler>/<path:path>'
                 ], type='http', auth="public", website=True, sitemap=False)
    def naac_attachment(self, category, subcategory, handler, path=None, filename=None, xmlid=None,
                        model='ir.attachment', id=None,
                        field='datas', filename_field='name', unique=None, mimetype=None, download=None, data=None,
                        token=None, access_token=None, **kw):
        handler_id = False
        subcategory_id = request.env['naac.subcategory'].sudo().search([('name', '=', subcategory)], limit=1)

        if subcategory_id.category_id.name == category:
            if path:
                handler += '/' + path
            handler_id = request.env['naac.attachment.handler'].sudo().search(
                [('name', '=', handler), ('subcategory_id', '=', subcategory_id.id)], limit=1)
        if handler_id and handler_id.doc_attachment_ids:
            return request.env['ir.http']._get_content_common(xmlid=xmlid, model=model,
                                                              res_id=handler_id.doc_attachment_ids.ids[0],
                                                              field=field, unique=unique,
                                                              filename=filename,
                                                              filename_field=filename_field, download=False,
                                                              mimetype=mimetype, access_token=access_token, token=token)
        else:
            return request.render('website.page_404', {})

    @http.route(['/iqac/<string:category>/<string:handler>',
                 '/iqac/<string:category>/<string:handler>/<path:path>'
                 ], type='http', auth="public", website=True, sitemap=False)
    def iqac_attachment(self, category, handler, path=None, filename=None, xmlid=None,
                        model='ir.attachment', id=None,
                        field='datas', filename_field='name', unique=None, mimetype=None, download=None, data=None,
                        token=None, access_token=None, **kw):
        handler_id = False
        category_id = request.env['iqac.category'].sudo().search([('name', '=', category)], limit=1)
        if path:
            handler += '/' + path
        if category_id:
            handler_id = request.env['iqac.attachment.handler'].sudo().search(
                [('name', '=', handler), ('category_id', '=', category_id.id)], limit=1)
            if handler_id and handler_id.doc_attachment_ids:
                return request.env['ir.http']._get_content_common(xmlid=xmlid, model=model,
                                                                  res_id=handler_id.doc_attachment_ids.ids[0],
                                                                  field=field, unique=unique, filename=filename,
                                                                  filename_field=filename_field, download=False,
                                                                  mimetype=mimetype, access_token=access_token,
                                                                  token=token)
            else:
                return request.render('website.page_404', {})
        else:
            return request.render('website.page_404', {})
