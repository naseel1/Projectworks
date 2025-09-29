from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    _inherit = 'res.users'

    user_department_id = fields.Many2one(
        'website.department',
        string="Allowed Department",
        help="Restrict access to a specific department for this user.",
        ondelete='set null'
    )

    department_access_level = fields.Selection([
        ('own', 'Own Department Only'),
        ('full', 'Department Full Access'),
    ], string="Department Access")

    def is_admin_user(self):
        """Returns True if the user is part of the 'Settings' admin group."""
        return self.has_group('base.group_system')

    def write(self, vals):
        # Avoid interfering with system user or external APIs
        is_group_write = 'groups_id' in vals
        is_level_or_dept_write = 'department_access_level' in vals or 'user_department_id' in vals

        res = super().write(vals)

        # Prevent modifying groups unless department-level fields changed
        if not is_level_or_dept_write:
            return res

        full_group = self.env.ref('landing_page.group_allowed_department_admin', raise_if_not_found=False)
        own_group = self.env.ref('landing_page.group_allowed_department_user', raise_if_not_found=False)

        for user in self:
            # Allow all for admin
            if user.is_admin_user() or user.id == 1:
                if full_group and full_group.id not in user.groups_id.ids:
                    user.sudo().write({'groups_id': [(4, full_group.id)]})
                continue

            # Get latest values
            access = vals.get('department_access_level') or user.department_access_level
            department = vals.get('user_department_id') or user.user_department_id

            if access == 'own':
                if not department:
                    raise ValidationError("Users with 'Own Department Only' must have a department.")
                user.sudo().write({
                    'groups_id': [(3, full_group.id), (4, own_group.id)]
                })
            elif access == 'full':
                user.sudo().write({
                    'groups_id': [(3, own_group.id), (4, full_group.id)]
                })

        return res
