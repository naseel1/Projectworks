{
    'name': 'Announcement',
    'description': 'Announcement module',
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
        'security/news_announcement_security.xml',
        'security/ir.model.access.csv',
        'views/news_announcement_template.xml',
        'views/news_announcement_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'news-announcement/static/src/css/style.css',
        ],
    },

}
