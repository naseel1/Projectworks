
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class NssManage(models.Model):
    _name = "nss.manage"
    _description = "Nss Manage"

    nss_id = fields.Char(string="Nss ID", required=False, copy=False, index=True)
    incharge_name = fields.Char(string="Incharge Name")
    incharge_image = fields.Binary(string="Incharge Image", attachment=True)
    designation = fields.Char(string="Designation")
    activity_ids = fields.One2many("nss.activity", "nss_id", string="Activities")
    report_ids = fields.One2many('nss.report', 'nss_id', string="Reports")

    def name_get(self):
        return [(record.id, "NSS") for record in self]

    @api.model
    def create(self, vals):
        # Allow record creation only during install/update OR if no record exists
        if not self.env.context.get('install_mode') and self.search_count([]) >= 1:
            raise ValidationError("You can only have one NSS record.")
        return super().create(vals)


class NssReport(models.Model):
    _name = "nss.report"
    _description = "Nss Reports"

    report_title = fields.Char(string="Report Title")
    report_file = fields.Binary(string="Report File", attachment=True, required=True)
    report_filename = fields.Char(string="PDF File Name", compute="_compute_filename", store=True)
    nss_id = fields.Many2one("nss.manage", string="Nss", required=True, ondelete='cascade')

    @api.depends('report_title')
    def _compute_filename(self):
        for rec in self:
            if rec.report_title:
                clean_title = re.sub(r'[^\w\-_. ]', '', rec.report_title.strip())  # remove unwanted chars
                rec.report_filename = clean_title.replace(' ', '_') + '.pdf'
            else:
                rec.report_filename = 'report.pdf'


class NssActivity(models.Model):
    _name = "nss.activity"
    _description = "Nss Activities"

    nss_id = fields.Many2one("nss.manage", string="Nss", required=True, ondelete="cascade")
    activity_title = fields.Char(string="Activity Title", required=True)
    activity_description = fields.Text(string="Activity Description")
    image_ids = fields.One2many("nss.activity.image", "activity_id", string="Activity Images")


class NssActivityImage(models.Model):
    _name = "nss.activity.image"
    _description = "Nss Activity Images"

    activity_id = fields.Many2one("nss.activity", string="Activity", ondelete="cascade")
    image = fields.Binary(string="Image", attachment=True)
