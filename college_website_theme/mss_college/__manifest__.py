{
    'name': 'MSS College website',
    'description': 'MSS College website',
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

        'views/mss_header.xml',
        'views/mss_home.xml',
        'views/mss_footer.xml',
        'views/downloads.xml',

        # About Us
        'views/about_us/about.xml',
        'views/about_us/code_of_conduct.xml',
        'views/about_us/history.xml',
        'views/about_us/principal_message.xml',
        'views/about_us/staff_council.xml',

        # Academics
        'views/academics/academic_calender.xml',
        'views/academics/add_on_courses.xml',

        # Departments
        'views/departments/b_a_economics.xml',
        'views/departments/b_a_english .xml',
        'views/departments/b_com_finance.xml',
        'views/departments/b_sc_pychology.xml',
        'views/departments/bba.xml',

        # Facilities
        'views/facilities/badminton.xml',
        'views/facilities/basketball.xml',
        'views/facilities/cricket.xml',
        'views/facilities/football.xml',
        'views/facilities/sports.xml',
        'views/facilities/volleyball.xml',

        # Iqac
        'views/iqac/composition.xml',
        'views/iqac/objective.xml',

        # statutory_boards
        'views/statutory_boards/statutory_boards.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'mss_college/static/src/css/mss.css',
        ],
    },
}
