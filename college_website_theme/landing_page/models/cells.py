from odoo import models, fields, api
import re


class CellsManage(models.Model):
    _name = "cells.manage"
    _description = "Cells Manage"

    cell_id = fields.Char(string="Cell ID", required=False, copy=False, index=True)
    cell_name = fields.Char(string="Cell Name", required=True)
    cell_description = fields.Html(string="Cell Description")
    report_ids = fields.One2many('cells.report', 'cell_id', string="Reports")
    incharge_image = fields.Binary(string='Incharge Image', attachment=True,)
    incharge_name = fields.Char(string="Incharge Name",)


class CellsReport(models.Model):
    _name = "cells.report"
    _description = "Cells Reports"

    cell_id = fields.Many2one("cells.manage", string="Cells", ondelete='cascade')
    report_title = fields.Char(string="Report Title")
    report_file = fields.Binary(string="Report File", attachment=True, )
    report_filename = fields.Char(string="PDF File Name", compute="_compute_filename", store=True)

    @api.depends('report_title')
    def _compute_filename(self):
        for rec in self:
            if rec.report_title:
                clean_title = re.sub(r'[^\w\-_. ]', '', rec.report_title.strip())  # remove unwanted chars
                rec.report_filename = clean_title.replace(' ', '_') + '.pdf'
            else:
                rec.report_filename = 'report.pdf'
