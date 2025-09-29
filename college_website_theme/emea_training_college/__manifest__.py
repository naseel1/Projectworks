{
    'name': 'EMEA Training College website',
    'description': 'EMEA Training College website',
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

        'views/emea_header.xml',
        'views/emea_home.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'emea_training_college/static/src/css/style.css',
            'emea_training_college/static/src/js/header_menu_open.js',
        ],
    },
}
