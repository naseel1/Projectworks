{
    'name': 'Admission Manage',
    'description': 'Admission Data Manage ',
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
        'security/admission_manage_security.xml',
        'security/ir.model.access.csv',
        'views/admission_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },

}
