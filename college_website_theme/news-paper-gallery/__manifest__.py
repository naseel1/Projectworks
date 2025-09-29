{
    'name': 'News Paper Gallery',
    'description': 'News Paper Gallery Module',
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
        'security/image_gallery_security.xml',
        'security/ir.model.access.csv',
        'views/image_galleries_template.xml',
        'views/image_galleries_view.xml',

    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },

}
