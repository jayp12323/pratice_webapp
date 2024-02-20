import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template, form_template, file_upload_template = return_template.return_templates('page.tm', 'textarea.tm',
                                                                                       'form.tm', 'file_upload.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    dmesg_data = {"class": "div_pad font-weight-light", "leading_text": "DMESG Text", "textarea_id": "dmesg_text",
                  "name": "dmesg_text", "rows": "10", "button": True, "button_id": "dmesg_button",
                  "button_text": "Parse Dmesg Dates"}

    file_upload_data = {"class": "div_pad font-weight-light", "leading_text": "Or upload an DMESG File",
                        "file_upload_id": "dmesg_fileupload", "button": True, "button_id": "upload_dmesg_button",
                        "button_text": "Upload DMESG File"}

    dmesg_parsed_data = {"class": "font-weight-light hidden div_pad", "leading_text": "DMESG Parsed",
                         "textarea_id": "dmesg_parsed",
                         "name": "dmesg_parsed", "rows": "20"}

    dmesg_html = pystache.render(textarea_template, dmesg_data)
    file_upload_html = pystache.render(file_upload_template, file_upload_data)
    dmesg_parsed_html = pystache.render(textarea_template, dmesg_parsed_data)

    page_body_data = {'main_nav': main_nav_html, "body": dmesg_html + file_upload_html + dmesg_parsed_html,
                      "javascripts": [{"name": "dmesg.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
