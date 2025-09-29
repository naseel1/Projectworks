from odoo import models, fields, api


class WebsiteDepartment(models.Model):
    _name = 'website.department'
    _description = 'Website Department'

    dep_name = fields.Char(string="Department Name", required=True)
    dep_id = fields.Integer(string="Department ID")
    dep_image = fields.Image(string="Department Image")
    dep_description = fields.Html(string="Description")
    vision = fields.Text(string="Vision")
    mission = fields.Html(string="Mission")
    club_ids = fields.One2many('department.club.line', 'department_ids', string="Clubs")
    image_ids = fields.One2many('website.department.image', 'department_id', string="Gallery Images")
    programme_ids = fields.One2many('website.department.programme', 'department_id', string="Programmes Offered")

    def name_get(self):
        result = []
        for rec in self:
            display_name = f"{rec.dep_name or 'No Name'} ({rec.dep_id or '-'})"
            result.append((rec.id, display_name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """
        Alternative method for name search (used in newer Odoo versions)
        """
        if args is None:
            args = []

        domain = []
        if name:
            domain = ['|',
                      ('dep_name', operator, name),
                      ('dep_id', '=', name if name.isdigit() else 0)]

        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)


class WebsiteDepartmentProgramme(models.Model):
    _name = 'website.department.programme'
    _description = 'Department Programme'

    programme_id = fields.Char(string="Programme ID", readonly=True, copy=False, index=True)
    programme_name = fields.Char(string="Programme Name", required=True)
    programme_points = fields.Html(string="Programme Points")
    programme_description = fields.Html(string="Programme Description")
    department_id = fields.Many2one('website.department', string="Department", ondelete="cascade")
    syllabus_ids = fields.One2many('website.department.programme.syllabus', 'programme_id', string="Syllabus Files")
    programme_type = fields.Selection([
        ('ug', 'Undergraduate'),
        ('pg', 'Postgraduate'),
        ('research', 'Research')
    ], string="Programme Type", required=True)

    programme_category = fields.Selection([
        ('aided', 'Aided'),
        ('sf', 'Self Financing')
    ], string="Programme Category", required=False)

    @api.constrains('programme_id', 'department_id')
    def _check_unique_programme_id_per_department(self):
        for rec in self:
            if rec.programme_id and rec.department_id:
                duplicate = self.search([
                    ('programme_id', '=', rec.programme_id),
                    ('department_id', '=', rec.department_id.id),
                    ('id', '!=', rec.id)
                ], limit=1)
                if duplicate:
                    raise ValidationError("Programme ID must be unique within the same department.")

    @api.model
    def create(self, vals):
        if not vals.get('programme_id'):
            vals['programme_id'] = self.env['ir.sequence'].next_by_code('website.department.pgm.id') or '/'
        return super().create(vals)


class WebsiteDepartmentProgrammeSyllabus(models.Model):
    _name = 'website.department.programme.syllabus'
    _description = 'Programme Syllabus File'

    name = fields.Char(string="Title")
    syllabus_pdf = fields.Binary(string="Syllabus PDF", attachment=True, required=True)
    syllabus_filename = fields.Char(string="PDF Filename")
    syllabus_url = fields.Char(string="Syllabus URL", help="Provide a URL if the syllabus is hosted externally.")
    programme_id = fields.Many2one('website.department.programme', string="Programme", ondelete="cascade")

    @api.constrains('syllabus_pdf', 'syllabus_url')
    def _check_pdf_or_url(self):
        for record in self:
            if not record.syllabus_pdf and not record.syllabus_url:
                raise ValidationError("Please provide either a PDF or a URL for the syllabus.")


class WebsiteDepartmentImage(models.Model):
    _name = 'website.department.image'
    _description = 'Department Gallery Image'

    image = fields.Image(string="Image")
    department_id = fields.Many2one('website.department', string="Department", ondelete="cascade")
