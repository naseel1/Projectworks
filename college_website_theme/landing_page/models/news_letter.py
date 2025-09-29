from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class NewsLetter(models.Model):
    _name = "news.letter"
    _description = 'News Letter Model'

    title = fields.Char('Title', tracking=True, required=True)
    news_image = fields.Binary(string='Image', attachment=True, required=True)
    file_name = fields.Char('PDF File Name', tracking=True)
    file_data = fields.Binary('Upload File', attachment=True)
    url = fields.Char('URL', store=True)

    @api.model
    def create(self, vals):
        # Generate a file name based on name or another unique identifier if not provided
        if not vals.get('file_name') and vals.get('title'):
            vals['file_name'] = re.sub(r'\W+', '', vals['title']).lower() + '.pdf'

        # Call the super method to create the record
        record = super(NewsLetter, self).create(vals)

        # Logic to generate the file URL (if needed)
        if record.file_data:
            # Store the attachment in ir.attachment and set public=True
            attachment = self.env['ir.attachment'].create({
                'name': record.file_name,
                'type': 'binary',
                'datas': record.file_data,
                'res_model': self._name,
                'res_id': record.id,
                'mimetype': 'application/pdf',
                'public': True,  # Ensure the attachment is publicly accessible
            })
            # Generate the public URL
            record.url = '/web/content/%s/%s' % (attachment.id, record.file_name)

        return record

    def write(self, vals):
        # Call the super method to update the record
        res = super(NewsLetter, self).write(vals)

        # Update the URL if the file has been updated
        if 'file_data' in vals:
            for record in self:
                if record.file_data:
                    # Update the attachment in ir.attachment and set public=True
                    attachment = self.env['ir.attachment'].create({
                        'name': record.file_name,
                        'type': 'binary',
                        'datas': record.file_data,
                        'res_model': self._name,
                        'res_id': record.id,
                        'mimetype': 'application/pdf',
                        'public': True,  # Ensure the attachment is publicly accessible
                    })
                    # Regenerate the public URL
                    record.url = '/web/content/%s/%s' % (attachment.id, record.file_name)

        return res
