from odoo import http
from odoo.http import request
import io
from reportlab.pdfgen import canvas
from odoo.tools.safe_eval import safe_eval


class PaymentReceiptController(http.Controller):

    @http.route('/payment/receipt/<int:payment_id>', type='http', auth="user", website=True)
    def download_payment_receipt(self, payment_id, **kwargs):
        payment = request.env['account.payment'].sudo().browse(payment_id)

        if not payment.exists():
            return request.not_found()

        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.drawString(100, 750, f"Payment Receipt for: {payment.partner_id.name}")
        pdf.drawString(100, 730, f"Payment Amount: {payment.amount} {payment.currency_id.name}")
        pdf.drawString(100, 710, f"Payment Date: {payment.payment_date}")
        pdf.drawString(100, 690, f"Transaction ID: {payment.name}")
        pdf.save()

        pdf_value = buffer.getvalue()
        buffer.close()

        pdf_headers = [
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', f'attachment; filename=payment_receipt_{payment_id}.pdf')
        ]

        return request.make_response(pdf_value, headers=pdf_headers)
