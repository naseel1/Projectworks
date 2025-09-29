{
    'name': 'HDFC Payment Gateway',
    'version': '16.0',
    'summary': 'HDFC Payment Gateway Integration for Odoo',
    'category': "Website",
    'depends': ['payment', 'base', 'embase_website', ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/payment_provider_views.xml',
        'views/payment_records.xml',
        'views/payment_success.xml',
        # 'views/onboarding_payment_record_view.xml',
        'views/failed.xml',
        'views/pending.xml',
        'report/payment_report.xml',
        'views/payment_receipt_template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
