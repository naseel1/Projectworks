{
    'name': 'Mazharul Uloom College',
    'description': 'Mazharul Uloom College website',
    'category': 'Theme',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['website', 'web',
                'base_setup', 'landing_page', 'iqac_management', ],

    'images': [
    ],

    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [

        'views/mazharul_uloom_header.xml',
        'views/mazharul_uloom_home.xml',
        'views/mazharul_uloom_footer.xml',
        'views/faculty_profile.xml',
        'views/programme_detail.xml',
        'views/news_events.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'mazharul_uloom_college/static/src/css/mazharul_uloom.css',
        ],
    },
}
