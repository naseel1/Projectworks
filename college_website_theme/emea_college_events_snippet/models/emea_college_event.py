from odoo import models, fields


class MesCollegeEvent(models.Model):
    _inherit = "blog.post"

    event_description = fields.Html('Description')
    is_homepage = fields.Boolean('Latest Event Published in Homepage')
    is_highlight = fields.Boolean('Highlight Event in Homepage')
    is_achievements = fields.Boolean(' Achievements Published in HomePage')
    event_image = fields.Binary(string='Event Image', attachment=True, )
    event_location = fields.Char(string='Event Location')
    event_date = fields.Date(string='Upcoming Event Date')
