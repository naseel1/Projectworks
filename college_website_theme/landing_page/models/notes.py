from odoo import models, fields, api
from odoo.exceptions import ValidationError


class NotesUpdate(models.Model):
    _name = "notes.update"
    _description = "Notes Update"

    notes_title = fields.Char('Department Name', required=True)
    semester1_ids = fields.One2many('notes.pdf.file', 'notes_id_sem1', string="Semester 1 Notes")
    semester2_ids = fields.One2many('notes.pdf.file', 'notes_id_sem2', string="Semester 2 Notes")
    semester3_ids = fields.One2many('notes.pdf.file', 'notes_id_sem3', string="Semester 3 Notes")
    semester4_ids = fields.One2many('notes.pdf.file', 'notes_id_sem4', string="Semester 4 Notes")
    semester5_ids = fields.One2many('notes.pdf.file', 'notes_id_sem5', string="Semester 5 Notes")
    semester6_ids = fields.One2many('notes.pdf.file', 'notes_id_sem6', string="Semester 6 Notes")


class NotesPdfFile(models.Model):
    _name = 'notes.pdf.file'
    _description = 'Notes PDF File'

    name = fields.Char(string="Note Title", required=True)
    notes_pdf = fields.Binary(string="PDF File", attachment=True)
    url = fields.Char(string="External URL")

    # Reference to each semester slot (only one of these should be used per row)
    notes_id_sem1 = fields.Many2one('notes.update', string="Semester 1 Ref")
    notes_id_sem2 = fields.Many2one('notes.update', string="Semester 2 Ref")
    notes_id_sem3 = fields.Many2one('notes.update', string="Semester 3 Ref")
    notes_id_sem4 = fields.Many2one('notes.update', string="Semester 4 Ref")
    notes_id_sem5 = fields.Many2one('notes.update', string="Semester 5 Ref")
    notes_id_sem6 = fields.Many2one('notes.update', string="Semester 6 Ref")

    @api.constrains('notes_pdf', 'url')
    def _check_pdf_or_url(self):
        for record in self:
            if not record.notes_pdf and not record.url:
                raise ValidationError("Provide either a PDF or a URL.")

