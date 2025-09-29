{
    'name': 'SSR Price Plan',
    'description': 'SSR Price plan Manage ',
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
        'security/ssr_price_plan_manage_security.xml',
        'security/ir.model.access.csv',
        'views/ssr_price_plan_views.xml',

    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },

}
