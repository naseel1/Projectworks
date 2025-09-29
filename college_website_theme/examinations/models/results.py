from odoo import models, fields


class ExaminationResults(models.Model):
    _name = "exam.results"
    _description = "Examination Results"

    pdf_file = fields.Binary(string="Document", attachment=True)
    file_name = fields.Char(string="File Name")
    title = fields.Html(string="Title")
    date = fields.Date(string="Date")
