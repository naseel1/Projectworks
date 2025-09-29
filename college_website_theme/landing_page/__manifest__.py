{
    'name': 'Landing Page ',
    'description': 'Landing Page ',
    'category': 'Theme',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['website', 'web', 'base', 'base_setup', ],

    'images': [
    ],

    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'installable': True,

    'data': [
        'security/landing_page_security.xml',
        'security/website-department_rule.xml',
        'security/ir.model.access.csv',
        'views/landing_page_view.xml',
        'views/department_page_view.xml',
        'views/cpa_res_user_views.xml',
        'views/department_template.xml',
        'views/programme_detail.xml',
        'data/programme_id.xml',
        'views/template_notes_detail.xml',
        'views/template_notes_semester_detail.xml',
        'views/notes_page_views.xml',
        'views/academic_calendar_views.xml',
        'views/clubs_views.xml',
        'views/template_club.xml',
        'views/cells_views.xml',
        'views/associations_views.xml',
        'views/template_association_details.xml',
        'data/pta_data.xml',
        'views/pta_views.xml',
        'data/default_department.xml',
        'views/facilities_views.xml',
        'views/facilities_template.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'cpa/static/src/css/cpa.css',
            'cpa/static/src/css/cpa-home.css',
        ],
    },

}
