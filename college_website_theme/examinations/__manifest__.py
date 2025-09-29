{
    'name': 'Examinations',
    'description': 'Examinations Data Manage ',
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
        'security/examinations_manage_security.xml',
        'security/ir.model.access.csv',
        'views/examinations_views.xml',
        'views/notice_board_views.xml',
        'views/ese_views.xml',
        'views/exam_results_views.xml',

    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },

}
