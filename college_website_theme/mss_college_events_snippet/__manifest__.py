# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2021 PIT Solutions (<https://www.pitsolutions.ch>). All Rights Reserved.
#       Developer : Nikhil Krishnan (<nikhil.kn@pitsolutions.com>)
#
###################################################################################################

{
    "name": "mss_college_events_snippet",
    "description": """ MSS COLLEGE EVENTS SNIPPET""",
    "summary": "Mss College Events Snippet",
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
        'views/mss_college_events.xml',
        # snippets
        'views/snippets/event_mss_college_home1_view.xml',


    ],
    'assets': {
        'web.assets_frontend': [
             'mss_college_events_snippet/static/src/css/mincetech_website.css',
             'mss_college_events_snippet/static/src/scss/snippet.scss',
        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}
