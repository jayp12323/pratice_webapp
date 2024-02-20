import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, start_template, buttons_template = return_template.return_templates('page.tm', 'start.tm',
                                                                                       'buttons.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    body_data = {"functions": [
        {"link": "dmesg", "display": "DMESG Parsing"},
        {"link": "vizoozie", "display": "Vizoozie for Oozie XML"},
        {"link": "dotpdf", "display": "Convert Hive Dot to PDF"},
        {"link": "audit", "display": "Audit Timestamp Parsing"},
        {"link": "authlocal", "display": "Auth to Local"},
        {"link": "revisions", "display": "Revisions"}
    ]}
    body_html = pystache.render(start_template, body_data)

    page_body_data = {'main_nav': main_nav_html, "body": body_html}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
