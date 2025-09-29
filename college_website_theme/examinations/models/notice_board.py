from odoo import models, fields


class NoticeBoard(models.Model):
    _name = "notice.board"
    _description = "Notice Board"

    pdf_file = fields.Binary(string="Document", attachment=True)
    file_name = fields.Char(string="File Name")
    title = fields.Html(string="Title")
