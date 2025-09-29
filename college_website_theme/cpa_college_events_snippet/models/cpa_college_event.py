from odoo import models, fields


class MesCollegeEvent(models.Model):
    _inherit = "blog.post"

    event_description = fields.Html('Description')
    event_image = fields.Binary(string='Event Image', attachment=True, )
    is_event = fields.Boolean('Published in Event')
    is_newses = fields.Boolean('Published in News')
