{
    'name': 'AQAR Attachment Handler',
    'description': 'AQAR Attachment Handler On website',
    'category': 'Theme',
    'sequence': 1,
    'version': '15.0.1.0.0',
    'depends': ['website', 'web',
                'base_setup', ],

    'images': [
    ],

    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [
        'security/aqar_security.xml',
        'security/ir.model.access.csv',
        'views/aqar_attachment_template.xml',
        'views/aqar_attachment_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'aqar_attachment_handler/static/src/css/style.css',
        ],
    },

}
