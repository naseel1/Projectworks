from odoo import models, fields


class AcademicCalendar(models.Model):
    _name = "academic.calendar"
    _description = "Academic Calendar"

    pdf_file = fields.Binary(string="Document", attachment=True)
    file_name = fields.Char(string="File Name")
    academic_year = fields.Selection([
        ('2025-2026', '2025-2026'),
        ('2024-2025', '2024-2025'),
        ('2023-2024', '2023-2024'),
        ('2022-2023', '2022-2023'),
        ('2021-2022', '2021-2022'),
    ], string="Academic Year", required=True)
