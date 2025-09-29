import re
from odoo import models, fields, api


class StudentVoice(models.Model):
    _name = "student.voice"
    _description = 'Student Voice Model'

    student_name = fields.Char('Name', tracking=True, required=True)
    student_image = fields.Binary(string='Image', attachment=True, required=True)
    student_description = fields.Char('Description', tracking=True, required=True)
    batch = fields.Char('Batch', tracking=True, required=True)
