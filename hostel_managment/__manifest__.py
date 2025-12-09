{
    'name': "Hostel Management",
    'summary': "Hostel management made easy",
    'description': "Efficiently manage the entire residential facility",
    'author': "Adnan",
    'version': "17.0.1.0",
    'depends': ['base', 'report_xlsx'],
    'data': [
        'security/hostel_security.xml',
        'security/ir.model.access.csv',
        'reports/hostel_report_action.xml',
        'reports/hostel_report_template.xml',
        'views/hostel_hostel.xml',
        'views/hoste_room_view.xml',
        'views/hostel_student_view.xml',
        'views/hostel_amenities_view.xml',
        'views/category_hostel_view.xml',
        'wizards/xlsx_wizard_popup.xml',
        'wizards/xlsx_report_action.xml',

    ],
    'assets': {
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
