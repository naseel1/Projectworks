from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PtaManage(models.Model):
    _name = "pta.manage"
    _description = "PTA Info"

    incharge_name = fields.Char(string="Incharge Name")
    incharge_image = fields.Binary(string="Incharge Image", attachment=True)
    report_ids = fields.One2many("pta.report", "pta_id", string="PTA Reports")
    designation = fields.Char(string="Designation")

    def name_get(self):
        return [(record.id, "PTA") for record in self]

    @api.model
    def create(self, vals):
        # Allow record creation only during install/update OR if no record exists
        if not self.env.context.get('install_mode') and self.search_count([]) >= 1:
            raise ValidationError("You can only have one PTA record.")
        return super().create(vals)


class PtaReport(models.Model):
    _name = "pta.report"
    _description = "PTA Reports"

    pta_id = fields.Many2one("pta.manage", ondelete="cascade", string="PTA")
    report_title = fields.Char(string="Title")
    report_file = fields.Binary(string="PDF File", attachment=True)
    report_filename = fields.Char(string="Filename")
