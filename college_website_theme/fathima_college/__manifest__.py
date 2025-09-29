{
    'name': 'Fathima College website',
    'description': 'Fathima College website',
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
        # main section
        'views/fathima_header.xml',
        'views/fathima_home.xml',
        'views/fathima_footer.xml',
        # About Sections
        'views/about_us/about.xml',
        'views/about_us/management.xml',
        'views/about_us/administration.xml',
        'views/about_us/principal_message.xml',
        'views/about_us/former-principals.xml',
        'views/about_us/code_of_conduct_hostel.xml',
        'views/about_us/code_of_conduct_students.xml',
        'views/about_us/code_of_conduct_staff.xml',
        'views/about_us/core-values.xml',
        'views/about_us/perspective-plan.xml',
        'views/about_us/quality-policy.xml',
        'views/about_us/strategic-plan.xml',

        # Admission Sections
        'views/admission/admission_procedure.xml',
        'views/admission/scholarships.xml',
        'views/admission/fee_structure.xml',

        # Academics Sections
        'views/academics/programmes.xml',

        # Departments
        'views/departments/commerce/commerce.xml',
        'views/departments/commerce/commerce_faculty.xml',
        'views/departments/commerce/commerce_programmes.xml',
        'views/departments/commerce/commerce_activities.xml',
        'views/departments/commerce/commerce_report.xml',

        # IQAC
        'views/iqac/composition.xml',
        'views/iqac/naac-certificates.xml',
        'views/iqac/naac-ssr.xml',
        'views/iqac/naac-quality-profile.xml',
        'views/iqac/aqar.xml',
        'views/iqac/nirf.xml',
        'views/iqac/aishe.xml',
        'views/iqac/ariia.xml',
        'views/iqac/minutes-atr.xml',
        'views/iqac/iqac-activities.xml',
        'views/iqac/sss.xml',
        'views/iqac/feedback-report.xml',
        'views/iqac/subject-feedback.xml',
        'views/iqac/faculty-feedback.xml',
        'views/iqac/infrastructure-feedback.xml',
        'views/iqac/student-feedback.xml',

        # statutory_cells
        'views/statutory_cells/pta-committee.xml',
        'views/statutory_cells/anti-narcotic-cell.xml',
        'views/statutory_cells/anti-ragging-cell.xml',
        'views/statutory_cells/grievance-cell.xml',
        'views/statutory_cells/women-cell.xml',

        # facilities
        'views/facilities/amenities.xml',
        'views/facilities/it.xml',
        'views/facilities/physical.xml',
        'views/facilities/sports.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'fathima_college/static/src/css/fathima.css',
            'fathima_college/static/src/js/video.js',
            'fathima_college/static/src/js/download-doc.js',
        ],
    },
}
