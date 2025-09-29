import json
import requests
import base64
import random
import string
import io
from io import BytesIO
from odoo import http
from odoo.http import request
from odoo.modules.module import get_module_resource
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os


class HDFCPaymentController(http.Controller):

    @http.route(['/payment/<int:customer_id>/<string:package_name>'], type='http', auth='public', methods=['GET'],
                csrf=False)
    def hdfc_payment(self, customer_id, package_name, **kwargs):
        """Initiates the payment and redirects to HDFC Payment Page."""

        # Fetch the latest OTP verification record using the route customer_id
        otp_record = request.env['otp.verification'].sudo().search(
            [('customer_id', '=', customer_id)], order="create_date desc", limit=1)

        if not otp_record or not otp_record.customer_id:
            return request.redirect('/ssr/get_started')

        # 🔹 Fetch package info dynamically from ssr.plan model
        plan = request.env['ssr.plan'].sudo().search(
            [('plan_type', '=', package_name)], limit=1)

        if not plan:
            return "Invalid package selected"

        package_label = plan.name
        amount = plan.total_price  # take GST-included price

        if not amount:
            return "Invalid package selected"

        # Use separate variables to avoid conflicts
        customer_email = otp_record.email
        customer_phone = otp_record.contact_number
        customer_id_str = otp_record.customer_id  # keep original ID from OTP record
        first_name = otp_record.admin_name or "Customer"
        institution_name = otp_record.institution_name
        institution_domain = otp_record.institution_domain
        sub_domain = otp_record.institution_ssr
        address = otp_record.address

        # Generate a unique order ID
        order_id = "ORD-" + ''.join(random.choices(string.digits, k=10))

        provider = request.env['payment.provider_hdfc'].sudo().search([('state', '=', 'confirm')], limit=1)
        if not provider:
            return "Payment provider configuration not found"

        api_key = provider.api_key
        url = f"{provider.base_url}/session?client_auth_token={api_key}"
        merchant_id = provider.hdfc_merchant_id
        client_id = provider.hdfc_client_id

        encoded_auth = base64.b64encode(f"{api_key}:".encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_auth}",
            "x-merchantid": merchant_id,
            "x-customerid": client_id,
            "Content-Type": "application/json"
        }

        payload = {
            "order_id": order_id,
            "amount": str(amount),
            "customer_id": customer_id_str,
            "customer_email": customer_email,
            "customer_phone": customer_phone,
            "payment_page_client_id": client_id,
            "action": "paymentPage",
            "return_url": 'https://egov.embase.in/payment_details',
            "description": "Complete your payment",
            "first_name": first_name,
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("payment_links"):
                payment_link = response_data["payment_links"].get("web")
                if payment_link:
                    # Store SSR payment record
                    request.env['payment.ssr'].sudo().create({
                        'order_id': order_id,
                        'amount': amount,
                        'customer_id': customer_id_str,
                        'customer_email': customer_email,
                        'customer_phone': customer_phone,
                        'payment_status': 'pending',
                        "first_name": first_name,
                        "institution_name": institution_name,
                        "institution_domain": institution_domain,
                        "sub_domain": sub_domain,
                        "package_prices": package_label,
                        "address": address,
                    })
                    return request.redirect(payment_link, local=False)

            return f"Payment link not found: {response.text}"

        except requests.exceptions.RequestException as e:
            return f"Request error: {str(e)}"
        except json.JSONDecodeError as e:
            return f"JSON decode error: {str(e)} - Response: {response.text}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    @http.route(['/onboarding/payment/direct'], type='http', auth='public', methods=['POST'], csrf=False)
    def hdfc_payment_direct(self, **post):
        """Single-route onboarding payment: handle billing, initiate HDFC, redirect."""
        try:
            session_customer_id = request.session.get('customer_id')
            if not session_customer_id:
                return request.redirect('/get_started')

            plan_name = post.get('plan_name')
            billedto = post.get('billedto', '')
            address = post.get('address', '')
            gstin = post.get('gstin', '')

            # Safely convert amount to float
            try:
                amount = float(post.get('total_amount') or 0)
            except (ValueError, TypeError):
                return "Invalid amount format"

            # Validate input
            if not plan_name or amount <= 0:
                return "Invalid plan or amount"

            # Step 1: Get user from onboarding.verification
            record = request.env['onboarding.verification'].sudo().search(
                [('customer_id', '=', str(session_customer_id))], limit=1)
            if not record:
                return request.redirect('/get_started')

            customer_email = record.email
            customer_phone = record.phone_number
            customer_id_str = record.customer_id  # avoid overwriting
            first_name = record.name or "Customer"
            last_name = record.name or "Customer"
            institution_name = record.institution_name
            institution_domain = record.institution_domain
            sub_domain = record.sub_domain

            # Step 2: Generate order ID
            order_id = "ORD-" + ''.join(random.choices(string.digits, k=10))

            # Step 3: Prepare HDFC API
            provider = request.env['payment.provider_hdfc'].sudo().search([('state', '=', 'confirm')], limit=1)
            if not provider:
                return "Payment provider configuration not found"

            api_key = provider.api_key
            url = f"{provider.base_url}/session?client_auth_token={api_key}"
            merchant_id = provider.hdfc_merchant_id
            client_id = provider.hdfc_client_id
            encoded_auth = base64.b64encode(f"{api_key}:".encode()).decode()

            headers = {
                "Authorization": f"Basic {encoded_auth}",
                "x-merchantid": merchant_id,
                "x-customerid": client_id,
                "Content-Type": "application/json"
            }

            payload = {
                "order_id": order_id,
                "amount": str(amount),
                "customer_id": customer_id_str,  # safe
                "customer_email": customer_email,
                "customer_phone": customer_phone,
                "payment_page_client_id": client_id,
                "action": "paymentPage",
                "return_url": 'https://egov.embase.in/payment_details',
                "description": "Complete your onboarding payment",
                "first_name": first_name,
                "last_name": last_name,
            }

            # Step 4: Call HDFC API and store payment record
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("payment_links"):
                payment_link = response_data["payment_links"].get("web")
                if payment_link:
                    request.env['payment.onboarding'].sudo().create({  # ✅ now onboarding model
                        'order_id': order_id,
                        'amount': amount,
                        'customer_id': customer_id_str,
                        'customer_email': customer_email,
                        'customer_phone': customer_phone,
                        'payment_status': 'pending',
                        'first_name': first_name,
                        'last_name': last_name,
                        'source_record_id': str(record.id),
                        'billedto': billedto,
                        'address': address,
                        'gstin': gstin,
                        "institution_name": institution_name,
                        "institution_domain": institution_domain,
                        "sub_domain": sub_domain,
                        "plan_name": plan_name,
                    })
                    return request.redirect(payment_link, local=False)

            return f"Payment link not found: {response.text}"

        except requests.exceptions.RequestException as e:
            return f"Request error: {str(e)}"
        except json.JSONDecodeError as e:
            return f"JSON decode error: {str(e)} - Response: {response.text if 'response' in locals() else 'No response'}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    @http.route('/payment_details', type='http', auth='public', website=True, methods=['POST', 'GET'], csrf=False)
    def payment_details(self, **kwargs):
        order_id = kwargs.get('order_id')
        if not order_id:
            return "Order ID not found in the response"

        # 1) Find payment record (SSR first, then Onboarding)
        payment_record = request.env['payment.ssr'].sudo().search([('order_id', '=', order_id)], limit=1)
        source = "ssr"
        if not payment_record:
            payment_record = request.env['payment.onboarding'].sudo().search([('order_id', '=', order_id)], limit=1)
            source = "onboarding"

        if not payment_record:
            return "Payment record not found"

        # 2) Provider
        provider = request.env['payment.provider_hdfc'].sudo().search([('state', '=', 'confirm')], limit=1)
        if not provider:
            return "Payment provider configuration not found"

        url = f"https://smartgateway.hdfcbank.com/orders/{order_id}"
        encoded_auth = base64.b64encode(f"{provider.api_key}:".encode()).decode()
        headers = {
            "Authorization": f"Basic {encoded_auth}",
            "x-merchantid": provider.hdfc_merchant_id,
            "x-customerid": provider.hdfc_client_id,
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response_data = response.json() if response.text else {}

            # 3) Extract status safely
            hdfc_status = str(response_data.get('status', '')).lower()
            payment_method_type = response_data.get('payment_method_type', 'N/A')
            amount = response_data.get('amount', payment_record.amount)

            if hdfc_status == "charged":
                new_status = "success"
            elif hdfc_status == "pending":
                new_status = "pending"
            else:
                new_status = "failed"

            # 4) Update record
            payment_record.sudo().write({
                'payment_status': new_status,
                'payment_date': fields.Datetime.now(),
                'amount': amount,
            })

            # 5) Send email with template (SSR or Onboarding)
            try:
                template_xmlid = "onboarding_payment_mail.mail.template" if source == "onboarding" else "ssr_payment_mail.mail.template"
                template = request.env.ref(template_xmlid, raise_if_not_found=False)
                if template and payment_record:
                    template.sudo().send_mail(payment_record.id, force_send=True)
            except Exception as e:
                # log but do not break flow
                _logger.warning("Payment success email could not be sent: %s", str(e))
            # don’t break if template missing

            # 6) Render correct template
            template_map = {
                "success": 'hdfc_payment_gateway.payment_success_template',
                "pending": 'hdfc_payment_gateway.payment_pending_template',
                "failed": 'hdfc_payment_gateway.payment_failed_template'
            }
            return request.render(template_map.get(new_status, template_map["failed"]), {
                'order_id': order_id,
                'payment_status': new_status.capitalize(),
                'payment_method_type': payment_method_type,
                'amount': amount
            })

        except requests.exceptions.RequestException:
            payment_record.sudo().write({'payment_status': 'failed'})
            return request.render('hdfc_payment_gateway.payment_failed_template', {
                'order_id': order_id,
                'payment_status': 'Failed',
                'payment_method_type': 'N/A',
                'amount': payment_record.amount
            })
        except Exception:
            payment_record.sudo().write({'payment_status': 'failed'})
            return request.render('hdfc_payment_gateway.payment_failed_template', {
                'order_id': order_id,
                'payment_status': 'Failed',
                'payment_method_type': 'N/A',
                'amount': payment_record.amount
            })

    @http.route('/payment/receipt/<string:order_id>', type='http', auth='public', website=True)
    def download_payment_receipt(self, order_id, **kwargs):
        try:
            # Fetch from SSR or Onboarding safely
            payment = request.env['payment.ssr'].sudo().search([('order_id', '=', order_id)], limit=1)
            if not payment:
                payment = request.env['payment.onboarding'].sudo().search([('order_id', '=', order_id)], limit=1)
                if not payment:
                    return request.not_found()

            buffer = BytesIO()
            pdf = canvas.Canvas(buffer, pagesize=A4)
            width, height = A4
            start_x, start_y = 50, height - 100
            line_spacing = 20

            # Logo
            logo_path = get_module_resource('hdfc_payment_gateway', 'static', 'img', 'embase-logo.png')
            if os.path.exists(logo_path):
                pdf.drawImage(ImageReader(logo_path), start_x, start_y, width=190, height=38)

            pdf.setFont("Helvetica-Bold", 18)
            pdf.drawCentredString(width / 2, start_y - 60, "INVOICE")

            pdf.setFont("Helvetica", 12)
            details = [
                ("Invoice Number:", payment.id or 'N/A'),
                ("Transaction ID:", payment.order_id or 'N/A'),
                ("Invoice Date:", payment.payment_date.strftime('%d-%m-%Y') if payment.payment_date else 'N/A'),
                ("Customer Name:", payment.first_name or 'N/A'),
                ("Customer Email:", payment.customer_email or 'N/A'),
                ("Customer Phone:", payment.customer_phone or 'N/A'),
                ("Invoice Paid:", f"{payment.amount or 'N/A'}"),
            ]

            y_position = start_y - 120
            for label, value in details:
                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(start_x, y_position, label)
                pdf.setFont("Helvetica", 12)
                pdf.drawString(start_x + 180, y_position, str(value))
                y_position -= line_spacing

            # Footer
            pdf.setFont("Helvetica", 10)
            pdf.drawString(start_x, y_position - 40, "Thank you for choosing our SSR Portal Services!")
            pdf.drawString(start_x, y_position - 60, "For queries, contact: billing@embase.in | +91 98765 43210")

            pdf.save()
            pdf_value = buffer.getvalue()
            buffer.close()

            return request.make_response(pdf_value, [
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'attachment; filename=payment_receipt_{order_id}.pdf')
            ])

        except Exception as e:
            return f"Error generating payment receipt: {str(e)}"
