{
    'name': 'CPA College',
    'description': 'CPA College website',
    'category': 'Theme',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['website', 'web',
                'base_setup', 'landing_page', ],

    'images': [
    ],

    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [

        'views/cpa_header.xml',
        'views/landing.xml',
        'views/cpa-home.xml',
        'views/cpa_footer.xml',
        'views/faculty_profile.xml',
        'views/event_detail.xml',
        'views/events.xml',
        'views/exam_results_view.xml',
        'views/res_config_settings.xml',
        'views/programme_detail.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'cpa/static/src/css/cpa.css',
            'cpa/static/src/css/cpa-home.css',
        ],
    },
}
