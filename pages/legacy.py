import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, text_template, form_template, file_upload_template, div_template = return_template.return_templates(
        'page.tm',
        'text.tm',
        'form.tm',
        'file_upload.tm',
        'div.tm')

    main_nav_html = return_main_nav_html.return_main_nav_html()

    legacy_data = {"class": "div_pad font-weight-bold", "leading_text": "Legacy Hortonworks Case #",
                   "text_id": "legacy_text", "name": "legacy_text", "button": True, "button_id": "legacy_button",
                   "button_text": "Return New Case #"}

    legacy_parsed_data = {"class": "font-weight-bold hidden div_pad", "leading_text": "New Cloudera Case",
                          "div_id": "legacy_parsed"}

    legacy_html = pystache.render(text_template, legacy_data)
    legacy_parsed_html = pystache.render(div_template, legacy_parsed_data)

    page_body_data = {'main_nav': main_nav_html,"body": legacy_html + legacy_parsed_html,
                      "javascripts": [{"name": "legacy.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
