from odoo import models, fields


class CareerManage(models.Model):
    _name = "career.manage"
    _description = "Career Manage"

    post_title = fields.Char('Title', tracking=True, required=True)
    available_post = fields.Integer('Post Available', tracking=True, required=True)
    job_description = fields.Char('Description', tracking=True, required=True)
    job_type = fields.Selection([('full_time', 'Full Time'), ('part_time', 'Part Time')], string='Job Type',
                                required=True)
    experience = fields.Integer('Experience', tracking=True, required=True)
    last_date = fields.Date('Last date of apply', tracking=True, required=True)
