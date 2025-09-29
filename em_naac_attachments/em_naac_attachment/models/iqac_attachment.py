# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2023 Emdot Mincetech Pvt. Ltd (<https://www.mincetech.com>). All Rights Reserved.
#       Developer : Nikhil Krishnan
#
##############################################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IQACCategory(models.Model):
    _name = "iqac.category"
    _description = 'IQAC Category'
    _order = 'sequence'
    _inherit = ['website.published.multi.mixin', 'mail.thread']


    _sql_constraints = [
        ('unique_iqac_category_name', 'UNIQUE(name)', 'Name must be unique!'),
    ]

    name = fields.Char(string='URL', required=True, tracking=True)
    title = fields.Char(string='Page Title', required=True, tracking=True)
    # url = fields.Char(string='URL', required=True, tracking=True)
    sequence = fields.Integer('Sequence', default=1)
    active = fields.Boolean(string='Active', default=True)

    website_published = fields.Boolean()
    is_published = fields.Boolean()
    published_date = fields.Datetime('Published Date')
    website_id = fields.Many2one('website', ondelete='cascade', string="Website")

    @api.model
    def create(self, vals):
        if vals.get('name'):
            if '/' in vals.get('name'):
                raise ValidationError(_("Category name not allowed to add '/'"))
        category = super(IQACCategory, self).create(vals)
        return category

    def write(self, vals):
        if vals.get('name'):
            if '/' in vals.get('name'):
                raise ValidationError(_("Category name not allowed to add '/'"))
        result = super(IQACCategory, self).write(vals)
        return result


class IQACAttachmentManager(models.Model):
    _name = "iqac.attachment.handler"
    _description = "IQAC Attachment Manager"
    _order = "sequence"

    _inherit = ['website.published.multi.mixin', 'mail.thread']

    @api.depends('name')
    def _compute_website_url(self):
        super(IQACAttachmentManager, self)._compute_website_url()
        for handler in self:
            handler.website_url = '/iqac/%s/%s' % ((handler.category_id.name), (handler.name))

    name = fields.Char(string='Name', required=True, tracking=True)
    title = fields.Char(string='Title', required=True, tracking=True)
    sequence = fields.Integer('Sequence', default=1)
    state = fields.Selection([('draft', 'Unpublished'), ('published', 'Published')], string="Status", default="draft",
                             tracking=True)
    active = fields.Boolean(default=True)
    category_id = fields.Many2one('iqac.category', string="Category")
    doc_attachment_ids = fields.Many2many('ir.attachment', 'iqac_attachment_handler_doc_rel', 'handler_doc_id',
                                          'attach_iqac_handler_id', string="Attachment",
                                          help='You can attach only one copy of your document.', copy=False)
    website_published = fields.Boolean()
    published_date = fields.Datetime('Published Date')
    website_id = fields.Many2one('website', ondelete='cascade', string="Website")

    _sql_constraints = [
        ('unique_iqac_attachment_handler_name', 'UNIQUE(name)', 'Name must be unique!'),
    ]


class IQACCategoryIrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        if vals.get('res_model') == 'iqac.attachment.handler':
            vals['public'] = True
        attachment = super(IQACCategoryIrAttachment, self).create(vals)
        return attachment
