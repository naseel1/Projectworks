from odoo import models, fields


class FathimaCollegeEvent(models.Model):
    _inherit = "blog.post"

    _description = fields.Html('Description')
    _image = fields.Binary(string='Event Image', attachment=True, )
    publish_date = fields.Date(string='Post Date')
