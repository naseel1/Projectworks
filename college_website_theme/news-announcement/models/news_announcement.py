import re
from odoo import models, fields, api


class NewsAnnouncement(models.Model):
    _name = "news.announcement"
    _description = 'News Announcement'

    title = fields.Char('Title', tracking=True, required=True)
    url = fields.Char(string="URL", store=True)