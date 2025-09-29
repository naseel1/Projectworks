from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class ScholarshipsManage(models.Model):
    _name = "scholarships.manage"
    _description = "Scholarships Manage"

    incharge_name = fields.Char(string="Incharge Name")
    incharge_image = fields.Binary(string="Incharge Image", attachment=True)
    designation = fields.Char(string="Designation")
    scholarship_ids = fields.One2many(
        "scholarship.item", "manage_id", string="Scholarships"
    )

    def name_get(self):
        return [(record.id, "Scholarships") for record in self]

    @api.model
    def create(self, vals):
        # Allow record creation only during install/update OR if no record exists
        if not self.env.context.get('install_mode') and self.search_count([]) >= 1:
            raise ValidationError("You can only have one NSS record.")
        return super().create(vals)


class ScholarshipItem(models.Model):
    _name = "scholarship.item"
    _description = "Scholarship Item"

    scholarship_name = fields.Char(string="Scholarship Name", required=True)
    website_url = fields.Char(string="Website URL")

    manage_id = fields.Many2one(
        "scholarships.manage", string="Scholarship Manage", ondelete="cascade"
    )
