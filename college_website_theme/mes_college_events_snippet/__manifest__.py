# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2021 PIT Solutions (<https://www.pitsolutions.ch>). All Rights Reserved.
#       Developer : Nikhil Krishnan (<nikhil.kn@pitsolutions.com>)
#
###################################################################################################

{
    "name": "Mes College Events Snippet",
    "description": """ Mes College Events Snippet""",
    "summary": "Mes College Events Snippet",
    "category": "Website/Website",
    "version": "15.0.1.0.1",
    'author': 'Naseel',
    'company': 'EM.Mincetech',
    'maintainer': 'Developer',
    'website': 'https://www.mincetech.com/',
    'depends': [
        'base_setup',
        'web_editor',
        'website',
        'website_blog',

    ],
    'data': [
        'views/mes_college_events.xml',
        # snippets
        'views/snippets/event_mes_college_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'mincetech_website_blog_snippet/static/src/scss/*.scss',
            # 'mincetech_website_blog_snippet/static/src/css/mincetech_website.css',
        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}
