from odoo import models, fields


class ExaminationCalendar(models.Model):
    _name = "examination.calendar"
    _description = "Examination Calendar"

    pdf_file = fields.Binary(string="Document", attachment=True)
    file_name = fields.Char(string="File Name")
    calendar_name = fields.Char(string="Name")
