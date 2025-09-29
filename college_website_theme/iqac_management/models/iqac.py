from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class IqacMain(models.Model):
    """Main IQAC Category – top-level container for items and subitems"""
    _name = 'iqac.main'
    _description = 'IQAC Main Category'

    name = fields.Char("Name", required=True)
    description = fields.Html("Description")
    item_ids = fields.One2many('iqac.item', 'main_id', string="IQAC Links")
    subitem_ids = fields.One2many('iqac.subitem', 'main_id', string="Sub Sections")
    iqac_id = fields.Char(string="IQAC ID", readonly=True, copy=False, index=True)
    public_url = fields.Char(string="Public Page URL", compute="_compute_public_url")

    @api.model
    def create(self, vals):
        """Auto-generate IQAC ID from sequence"""
        if not vals.get('iqac_id'):
            vals['iqac_id'] = self.env['ir.sequence'].next_by_code('iqac.item.seq') or '/'
        return super().create(vals)

    def _compute_public_url(self):
        """Generate public URL for each IQAC main"""
        for rec in self:
            if rec.iqac_id and rec.name:
                rec.public_url = f"/iqac/{rec.iqac_id}/{rec.name.replace(' ', '-').lower()}"
            else:
                rec.public_url = ""


class IqacItem(models.Model):
    """Child links/files under IQAC Main"""
    _name = 'iqac.item'
    _description = 'IQAC Item Entry'

    main_id = fields.Many2one('iqac.main', string="Category", required=True, ondelete='cascade')
    title = fields.Char("Name", required=True)
    url = fields.Char("External PDF URL")
    pdf_file = fields.Binary("Upload PDF", attachment=True)
    pdf_filename = fields.Char("PDF Filename")

    @api.constrains('url', 'pdf_file')
    def _check_url_or_file(self):
        """Ensure either a URL or a PDF is provided"""
        for rec in self:
            if not rec.url and not rec.pdf_file:
                raise ValidationError(_("You must provide either an external PDF URL or upload a PDF file."))


class IqacSubItem(models.Model):
    _name = 'iqac.subitem'
    _description = 'IQAC Sub Item'

    main_id = fields.Many2one('iqac.main', string="Parent IQAC Main", required=True, ondelete='cascade')
    name = fields.Char("Name", required=True)
    description = fields.Html("Description")
    subitem_id = fields.Char(string="Subitem ID", readonly=True, copy=False, index=True)
    public_url = fields.Char(string="Public Page URL", compute="_compute_public_url", store=True)
    attachment_ids = fields.One2many('iqac.subitem.attachment', 'subitem_id', string="Documents")

    @api.model
    def create(self, vals):
        if not vals.get('subitem_id'):
            vals['subitem_id'] = self.env['ir.sequence'].next_by_code('iqac.subitem.seq') or '/'
        return super().create(vals)

    @api.depends('subitem_id', 'name')
    def _compute_public_url(self):
        for rec in self:
            if rec.subitem_id and rec.name:
                rec.public_url = f"/iqac-sub/{rec.subitem_id}/{rec.name.replace(' ', '-').lower()}"
            else:
                rec.public_url = ""


class IqacSubItemAttachment(models.Model):
    _name = 'iqac.subitem.attachment'
    _description = 'IQAC Sub Item Attachment'

    subitem_id = fields.Many2one('iqac.subitem', string="Sub Item", required=True, ondelete='cascade')
    title = fields.Char("Title", required=True)
    url = fields.Char("External PDF URL")
    file = fields.Binary("Upload PDF", attachment=True)
    file_name = fields.Char("File Name")

    @api.constrains('url', 'file')
    def _check_only_one_source(self):
        for rec in self:
            if rec.url and rec.file:
                raise ValidationError(_("Please provide either a URL or a PDF file, not both."))
