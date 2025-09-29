{
    'name': 'Scholarships',
    'description': 'Scholarships Manage Module',
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
        'security/scholarships_security.xml',
        'security/ir.model.access.csv',
        'data/scholarships_data.xml',
        'views/scholarship_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },

}
