from odoo import models, fields, api


class PaymentReceiptReport(models.AbstractModel):
    _name = "report.hdfc_payment_gateway.payment_receipt_template"
    _description = "Payment Receipt Report"

    def _get_report_values(self, docids, data=None):
        docs = self.env["payment.success"].browse(docids)
        return {
            "doc_ids": docids,
            "doc_model": "payment.success",
            "docs": docs,
        }
