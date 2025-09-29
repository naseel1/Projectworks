{
    'name': 'Nss Manage',
    'description': 'Nss Manage Module',
    'category': 'Theme',
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
        'security/nss_security.xml',
        'security/ir.model.access.csv',
        'data/nss_data.xml',
        'views/nss_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },

}
