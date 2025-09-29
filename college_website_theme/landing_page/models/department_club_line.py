from odoo import models, fields

class DepartmentClubLine(models.Model):
    _name = 'department.club.line'
    _description = 'Club ID Line'

    club_id = fields.Integer(string="Club ID")
    department_ids = fields.Many2one('website.department', string="Department", ondelete='cascade')