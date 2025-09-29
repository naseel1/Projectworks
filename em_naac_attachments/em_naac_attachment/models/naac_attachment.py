# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2023 Emdot Mincetech Pvt. Ltd (<https://www.mincetech.com>). All Rights Reserved.
#       Developer : Nikhil Krishnan
#
##############################################################################################

from odoo import api, fields, models, _
from odoo.addons.http_routing.models.ir_http import slug
# from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
# from sedd_addons.sedd15.user import to_naive_user_tz


class NaacCategory(models.Model):
    _name = "naac.category"
    _description = 'Business Procedures Page'
    _order = 'sequence'
    _inherit = ['website.published.multi.mixin', 'mail.thread']

    # @api.depends('name')
    # def _compute_website_url(self):
    #     super(NaacCategory, self)._compute_website_url()
    #     for procedure in self:
    #         procedure.website_url = '/naac/%s' % (slug(procedure))

    # @api.constrains('name')
    # def _check_category_name(self):
    #     for category in self:
    #         if category.name not in badge_user.user_id.employee_ids:
    #             raise ValidationError(_('The selected employee does not correspond to the selected user.'))

    _sql_constraints = [
        ('unique_naac_category_name', 'UNIQUE(name)', 'Name must be unique!'),
    ]

    name = fields.Char(string='URL', required=True, tracking=True)
    title = fields.Char(string='Page Title', required=True, tracking=True)
    # url = fields.Char(string='URL', required=True, tracking=True)
    sequence = fields.Integer('Sequence', default=1)
    active = fields.Boolean(string='Active', default=True)

    line_ids = fields.One2many('naac.subcategory', 'category_id', string='Category')
    website_published = fields.Boolean()
    is_published = fields.Boolean()
    published_date = fields.Datetime('Published Date')
    website_id = fields.Many2one('website', ondelete='cascade', string="Website")

    @api.model
    def create(self, vals):
        if vals.get('name'):
            if '/' in vals.get('name'):
                raise ValidationError(_("Category name not allowed to add '/'"))
        category = super(NaacCategory, self).create(vals)
        return category

    def write(self, vals):
        if vals.get('name'):
            if '/' in vals.get('name'):
                raise ValidationError(_("Category name not allowed to add '/'"))
        result = super(NaacCategory, self).write(vals)
        return result


class NaacSubCategory(models.Model):
    _name = "naac.subcategory"
    _description = "Naac Subcategory"
    _order = "sequence"

    _inherit = ['website.published.multi.mixin', 'mail.thread']

    # @api.depends('name')
    # def _compute_website_url(self):
    #     super(NaacSubCategory, self)._compute_website_url()
    #     for subcategory in self:
    #         subcategory.website_url = '/naac/%s/%s' % (slug(subcategory.category_id), slug(subcategory))

    name = fields.Char(string='Name', required=True, tracking=True)
    title = fields.Char(string='Title', required=True, tracking=True)
    sequence = fields.Integer('Sequence', default=1)
    # page_type = fields.Selection([('draft', 'Unpublished'), ('published', 'Published')], string="Type")
    state = fields.Selection([('draft', 'Unpublished'), ('published', 'Published')], string="Status", default="draft",
                             tracking=True)
    active = fields.Boolean(default=True)
    category_id = fields.Many2one('naac.category', string="Page")
    website_published = fields.Boolean()
    published_date = fields.Datetime('Published Date')
    website_id = fields.Many2one('website', ondelete='cascade', string="Website")

    @api.model
    def create(self, vals):
        if vals.get('name'):
            if '/' in vals.get('name'):
                raise ValidationError(_("SubCategory name not allowed to add '/'"))
        category = super(NaacSubCategory, self).create(vals)
        return category

    def write(self, vals):
        if vals.get('name'):
            if '/' in vals.get('name'):
                raise ValidationError(_("SubCategory name not allowed to add '/'"))
        result = super(NaacSubCategory, self).write(vals)
        return result

    _sql_constraints = [
        ('unique_naac_subcategory_name', 'UNIQUE(name)', 'Name must be unique!'),
    ]


class NaacAttachmentManager(models.Model):
    _name = "naac.attachment.handler"
    _description = "Naac Attachment Manager"
    _order = "sequence"

    _inherit = ['website.published.multi.mixin', 'mail.thread']

    @api.depends('name')
    def _compute_website_url(self):
        super(NaacAttachmentManager, self)._compute_website_url()
        for handler in self:
            handler.website_url = '/naac/%s/%s/%s' % ((handler.category_id.name), (handler.subcategory_id.name), (handler.name))

    name = fields.Char(string='Name', required=True, tracking=True)
    title = fields.Char(string='Title', required=True, tracking=True)
    sequence = fields.Integer('Sequence', default=1)
    state = fields.Selection([('draft', 'Unpublished'), ('published', 'Published')], string="Status", default="draft",
                             tracking=True)
    active = fields.Boolean(default=True)
    category_id = fields.Many2one('naac.category', string="Category")
    subcategory_id = fields.Many2one('naac.subcategory', string="Subcategory")
    doc_attachment_ids = fields.Many2many('ir.attachment', 'naac_attachment_handler_doc_rel', 'handler_doc_id',
                                          'attach_naac_handler_id', string="Attachment",
                                          help='You can attach only one copy of your document.', copy=False)
    website_published = fields.Boolean()
    published_date = fields.Datetime('Published Date')
    website_id = fields.Many2one('website', ondelete='cascade', string="Website")

    _sql_constraints = [
        ('unique_naac_attachment_handler_name', 'UNIQUE(name)', 'Name must be unique!'),
    ]


class NaacCategoryIrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        if vals.get('res_model') == 'naac.attachment.handler':
            vals['public'] = True
            # intranet_website = self.env['website'].search([], limit=1)
            # if intranet_website:
            #     vals['website_id'] = intranet_website.id
        attachment = super(NaacCategoryIrAttachment, self).create(vals)
        return attachment
