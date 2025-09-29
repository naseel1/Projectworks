from odoo import models, fields


class EndSemesterExamination(models.Model):
    _name = "end.semester"
    _description = "end.semester"

    pdf_file = fields.Binary(string="Document", attachment=True)
    file_name = fields.Char(string="File Name")
    title = fields.Html(string="Title")
