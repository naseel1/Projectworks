from odoo import models, fields, api
import re


class ClubsManage(models.Model):
    _name = "clubs.manage"
    _description = "Clubs Manage"

    club_id = fields.Char(string="Club ID", required=False, copy=False, index=True)
    club_name = fields.Char(string="Club Name", required=True)
    club_description = fields.Text(string="Club Description")
    report_ids = fields.One2many('clubs.report', 'club_id', string="Reports")
    club_image = fields.Binary(string='Image', attachment=True, )
    activity_ids = fields.One2many("club.activity", "club_id", string="Activities")


class ClubReport(models.Model):
    _name = "clubs.report"
    _description = "Club Reports"

    club_id = fields.Many2one("clubs.manage", string="Club", required=True, ondelete='cascade')
    report_title = fields.Char(string="Report Title")
    report_file = fields.Binary(string="Report File", attachment=True, required=True)
    report_filename = fields.Char(string="PDF File Name", compute="_compute_filename", store=True)

    @api.depends('report_title')
    def _compute_filename(self):
        for rec in self:
            if rec.report_title:
                clean_title = re.sub(r'[^\w\-_. ]', '', rec.report_title.strip())  # remove unwanted chars
                rec.report_filename = clean_title.replace(' ', '_') + '.pdf'
            else:
                rec.report_filename = 'report.pdf'


class ClubActivity(models.Model):
    _name = "club.activity"
    _description = "Club Activities"

    club_id = fields.Many2one("clubs.manage", string="Club", required=True, ondelete="cascade")
    activity_title = fields.Char(string="Activity Title", required=True)
    activity_description = fields.Text(string="Activity Description")
    image_ids = fields.One2many("club.activity.image", "activity_id", string="Activity Images")


class ClubActivityImage(models.Model):
    _name = "club.activity.image"
    _description = "Club Activity Images"

    activity_id = fields.Many2one("club.activity", string="Activity", ondelete="cascade")
    image = fields.Binary(string="Image", attachment=True)
