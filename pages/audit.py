import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template, form_template, file_upload_template = return_template.return_templates('page.tm', 'textarea.tm',
                                                                                       'form.tm','file_upload.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    audit_data = {"class": "div_pad font-weight-light", "leading_text": "Audit Text", "textarea_id": "audit_text",
                  "name": "audit_text", "rows": "10", "button": True, "button_id": "audit_button",
                  "button_text": "Parse Audit Timestamps"}

    file_upload_data = {"class": "div_pad font-weight-light", "leading_text": "Or upload an Audit File",
                        "file_upload_id": "audit_fileupload", "button": True, "button_id": "upload_audit_button",
                        "button_text": "Upload Audit File"}

    audit_parsed_data = {"class": "font-weight-light hidden div_pad", "leading_text": "Audit Timestamp Parsed",
                         "textarea_id": "audit_parsed",
                         "name": "audit_parsed", "rows": "20"}

    audit_html = pystache.render(textarea_template, audit_data)
    file_upload_html = pystache.render(file_upload_template, file_upload_data)
    audit_parsed_html = pystache.render(textarea_template, audit_parsed_data)

    page_body_data = {'main_nav': main_nav_html, "body": audit_html + file_upload_html+ audit_parsed_html,
                      "javascripts": [{"name": "audit.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
