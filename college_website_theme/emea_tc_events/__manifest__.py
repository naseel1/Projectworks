# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2021 PIT Solutions (<https://www.pitsolutions.ch>). All Rights Reserved.
#       Developer : Muhammad Naseel K
#
###################################################################################################

{
    "name": "EMEA Training College Events ",
    "description": """ EMEA Training College Events """,
    "summary": "EMEA Training College Events ",
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
        'views/emea_tc_events.xml',
        # snippets
        'views/snippets/event_emea_tc_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [

        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}
