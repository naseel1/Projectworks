# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2021 PIT Solutions (<https://www.pitsolutions.ch>). All Rights Reserved.
#       Developer : Nikhil Krishnan (<nikhil.kn@pitsolutions.com>)
#
###################################################################################################

{
    "name": "EMEA College Events Snippet",
    "description": """ EMEA College Events Snippet""",
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
        'views/emea_college_events.xml',
        # snippets
        'views/snippets/event_emea_college_home1_view.xml',
        'views/snippets/event_emea_college_home2_view.xml',
        'views/snippets/department_activities.xml',
        'views/snippets/achievements_home.xml',
        'views/snippets/news_home.xml',
        'views/snippets/upcoming_home.xml',
    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}
