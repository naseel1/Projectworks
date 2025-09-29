# -*- encoding: utf-8 -*-
##############################################################################################
#
#       Odoo, Open Source Management Solution
#       Copyright (C) 2023 Emdot mincetech (<https://www.mincetech.com>). All Rights Reserved.
#       Developer : Nikhil Krishnan (<nikhilkrishnan0101@gmail.com>)
#
###################################################################################################

{
    "name": "Portal Attachment Management",
    "description": """ Naac/Iqac Portal Attachment Management """,
    "summary": "Naac/Iqac Portal Attachment Management",
    "category": "Website/Website",
    "version": "16.0.1.0.1",
    'author': 'Nikhil Krishnan',
    'company': 'Mincetech',
    'maintainer': 'Mincetech',
    'website': 'https://www.mincetech.com',
    'depends': [
        'web_editor',
        'website',
    ],
    'data': [
        'security/naac_attachment_security.xml',
        'security/ir.model.access.csv',
        'views/naac_subcategory.xml',
        'views/naac_category.xml',
        'views/naac_attachment_handler.xml',
        'views/iqac_category.xml',
        'views/iqac_attachment_handler.xml',
        'views/intranet_menus.xml',
    ],
    # 'assets': {
    #     'web.assets_frontend': [
    #         'sedd_website_intranet/static/src/scss/intrnet_procedure_page.scss',
    #     ],
    # },

    'installable': True,
    'application': False,
    'auto_install': False,
}
