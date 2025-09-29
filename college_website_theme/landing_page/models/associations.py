from odoo import models, fields, api
import re


class AssociationManage(models.Model):
    _name = "association.manage"
    _description = "Association"

    association_name = fields.Char()
    association_description = fields.Html()
    incharge_name = fields.Char()
    incharge_image = fields.Binary(attachment=True)
    report_ids = fields.One2many("association.report", "association_id")
    activity_ids = fields.One2many("association.activity", "association_id")


class AssociationReport(models.Model):
    _name = "association.report"

    association_id = fields.Many2one("association.manage", ondelete="cascade")
    report_title = fields.Char()
    report_file = fields.Binary(attachment=True)
    report_filename = fields.Char()


class AssociationActivity(models.Model):
    _name = "association.activity"

    association_id = fields.Many2one("association.manage", ondelete="cascade")
    activity_title = fields.Char()
    activity_description = fields.Text()
    image_ids = fields.One2many("association.activity.image", "activity_id")


class AssociationActivityImage(models.Model):
    _name = "association.activity.image"

    activity_id = fields.Many2one("association.activity", ondelete="cascade")
    image = fields.Binary(string="Image", attachment=True)
