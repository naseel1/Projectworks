import re
from odoo import models, fields, api


class MediaGalleries(models.Model):
    _name = "media.galleries"
    _description = 'Media Gallery'

    name = fields.Char('Name', tracking=True, required=True)
    media_type = fields.Selection([
        ('video', 'Video'),
        ('youtube', 'YouTube URL')
    ], string="Video Type", default='video', required=True)
    video = fields.Binary(string="Video", attachment=True)
    youtube_url = fields.Char(string="YouTube URL")
    date = fields.Date('Date', required=True)
    url = fields.Char(string="File URL", compute="_compute_video_url", store=True)

    @api.depends("video")
    def _compute_video_url(self):
        """Generate and update the public URL for the uploaded video."""
        attachment_model = self.env["ir.attachment"]
        for record in self:
            if record.video:
                # Preprocess filename separately
                clean_name = re.sub(r'\W+', '_', record.name).lower()
                file_name = "{}.mp4".format(clean_name)

                # Check if an attachment already exists
                existing_attachment = attachment_model.search([
                    ("res_model", "=", self._name),
                    ("res_id", "=", record.id),
                    ("name", "=", file_name)
                ], limit=1)

                if existing_attachment:
                    # Update the existing attachment
                    existing_attachment.write({"datas": record.video})
                    attachment_id = existing_attachment.id
                else:
                    # Create a new attachment
                    attachment = attachment_model.create({
                        "name": file_name,
                        "type": "binary",
                        "datas": record.video,
                        "res_model": self._name,
                        "res_id": record.id,
                        "public": True,
                    })
                    attachment_id = attachment.id

                # Generate the public URL
                record.url = "/web/content/{}?download=false".format(attachment_id)
            else:
                record.url = False

    def get_youtube_embed_url(self):
        """Extract YouTube Video ID and generate embed URL"""
        if self.youtube_url:
            regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?\/\s]{11})"
            match = re.search(regex, self.youtube_url)
            if match:
                return f"https://www.youtube.com/embed/{match.group(1)}"
        return ""
