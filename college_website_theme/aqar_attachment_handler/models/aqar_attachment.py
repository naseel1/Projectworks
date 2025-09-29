from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class AQARAttachment(models.Model):
    _name = "aqar.attachment"
    _description = 'Aqar Attachment'

    name = fields.Char('Name', required=True, tracking=True)
    file_name = fields.Char('File Name', tracking=True)
    file_data = fields.Binary('Attach File', attachment=True)
    # file = fields.Binary('Upload File', attachment=True)
    url = fields.Char('URL', store=True)
    date = fields.Date('Date', required=True)
    year = fields.Selection(
        string='Year',
        selection=[
            ('2020-2021', '2020-2021'),
            ('2021-2022', '2021-2022'),
            ('2022-2023', '2022-2023'),
            ('2023-2024', '2023-2024'),
            ('2024-2025', '2024-2025'),
            # Add more ranges as needed
        ],
        required=True

    )

    @api.model
    def create(self, vals):
        # Generate a file name based on name or another unique identifier if not provided
        if not vals.get('file_name') and vals.get('name'):
            vals['file_name'] = re.sub(r'\W+', '', vals['name']).lower() + '.pdf'

        # Call the super method to create the record
        record = super(AQARAttachment, self).create(vals)

        # Logic to generate the file URL (if needed)
        if record.file_data:
            # Store the attachment in ir.attachment and generate a URL
            attachment = self.env['ir.attachment'].create({
                'name': record.file_name,
                'type': 'binary',
                'datas': record.file_data,
                'res_model': self._name,
                'res_id': record.id,
                'mimetype': 'application/pdf',
                'public': True,
            })
            record.url = '/web/content/%s/%s' % (attachment.id, record.file_name)

        return record

    def write(self, vals):
        # Call the super method to update the record
        res = super(AQARAttachment, self).write(vals)

        # Update the URL if file has been updated
        if 'file_data' in vals:
            for record in self:
                if record.file_data:
                    # Update the attachment in ir.attachment and regenerate the URL
                    attachment = self.env['ir.attachment'].create({
                        'name': record.file_name,
                        'type': 'binary',
                        'datas': record.file_data,
                        'res_model': self._name,
                        'res_id': record.id,
                        'mimetype': 'application/pdf',
                        'public': True,
                    })
                    record.url = '/web/content/%s/%s' % (attachment.id, record.file_name)

        return res
