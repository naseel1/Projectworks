{
    'name': 'PDF Uploader',
    'description': 'PDF Uploader On website',
    'category': 'Website/Website',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['website', 'web',
                'base_setup', ],

    'images': [
    ],

    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [
        'security/pdf_security.xml',
        'security/ir.model.access.csv',
        'views/pdf_uploader_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },

}
