from odoo import models, fields, api
import re


class NewsPaper(models.Model):
    _name = "news.paper"
    _description = 'News Paper'
    _order = 'create_date asc'

    row_number = fields.Integer(string='No.', compute='_compute_row_number', store=False)
    paper = fields.Binary(string="News Paper", attachment=True, required=True)
    date = fields.Date('Date')

    @api.depends('create_date')  # or any field that affects sorting
    def _compute_row_number(self):
        for index, record in enumerate(self.sorted(key=lambda r: r.create_date or r.id), start=1):
            record.row_number = index
