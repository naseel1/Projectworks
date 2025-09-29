from odoo import models, fields


class MSSCollegeEvent(models.Model):
    _inherit = "blog.post"

    blog_description = fields.Html('Description')
    blog_post_image = fields.Binary(string='Event Image', attachment=True, )
