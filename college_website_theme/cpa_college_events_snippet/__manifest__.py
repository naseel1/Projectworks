# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2025 . All Rights Reserved.
#       Developer : Naseel
#
###################################################################################################

{
    "name": "CPA College Events Snippet",
    "description": """ CPA College Events Snippet""",
    "summary": "CPA College Events Snippet",
    "category": "Website/Website",
    "version": "16.0.1.0.1",
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
        'views/cpa_college_events.xml',
        # snippets
        'views/snippets/event_cpa_college_view.xml',
        # 'views/snippets/news_mu_college.xml',
    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}
