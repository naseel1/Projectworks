{
    'name': 'Video Gallery',
    'description': 'Video Gallery Module',
    'category': 'Theme',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['website', 'web',
                'base_setup', ],
    'author': 'naseel',

    'images': [
    ],

    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'data': [
        'security/media_gallery_security.xml',
        'security/ir.model.access.csv',
        'views/media_galleries_template.xml',
        'views/media_galleries_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'media-gallery/static/src/css/style.css',
        ],
    },

}
