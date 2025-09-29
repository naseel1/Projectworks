{
    'name': "External Api Integration",
    'summary': """
       External Api Integration""",
    'description': """
        External Api Integration
    """,
    'author': "Mincetech",
    'license': 'LGPL-3',
    'website': "https://www.mincetech.com/",
    'category': "Website",
    'version': "0.1",
    'sequence': "1",
    'application': "True",
    'depends': [
        'website',
        'base_setup',
        'web',
        'base',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/api_configuration.xml',
    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },

}
