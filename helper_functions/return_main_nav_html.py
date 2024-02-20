import pystache
from helper_functions import return_template


def return_main_nav_html():
    main_nav_template, form_template = return_template.return_templates('main_nav.tm', 'form.tm')
    main_nav_data = {
        "functions": [{"link": "/dash", "display": "Back to Dashboard"},
                      {"link": "/dmesg", "display": "DMESG Parser"},
                      {"link": "/vizoozie", "display": "Vizoozie for Oozie XML"},
                      {"link": "/dotpdf", "display": "Hive Dot to PDF"},
                      {"link": "/audit", "display": "Audit Timestamp Parser"},
                      {"link": "/authlocal", "display": "Auth To Local"},
                      {"link": "/revisions", "display": "Revisions"}
        ]}
    main_nav_html = pystache.render(main_nav_template, main_nav_data)
    return main_nav_html
