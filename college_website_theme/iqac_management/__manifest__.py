{
    'name': 'IQAC Management ',
    'description': 'IQAC Management',
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
        'security/iqac_security.xml',
        'security/ir.model.access.csv',
        'views/iqac_views.xml',
        'data/iqac_sequence.xml',
        'views/iqac_template.xml',
        'data/iqac_sub.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'cpa/static/src/css/cpa.css',
            'cpa/static/src/css/cpa-home.css',
        ],
    },

}
