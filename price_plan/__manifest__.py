{
    'name': 'Onboarding Price Plan',
    'description': 'Onboarding Price plan Manage ',
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
        'security/price_plan_manage_security.xml',
        'security/ir.model.access.csv',
        'views/price_plan_views.xml',

    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },

}
