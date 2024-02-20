import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template, text_template, form_template, file_upload_template = return_template.return_templates('page.tm', 'textarea.tm', 'text.tm',
                                                                                       'form.tm', 'file_upload.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    principal_data = {"class": "div_pad font-weight-bold", "leading_text": "FQ Principal Name",
                   "text_id": "principal_text", "name": "principal_text"}

    authlocal_data = {"class": "div_pad font-weight-bold", "leading_text": "Auth to Local Rules", "textarea_id": "authlocal_text",
                  "name": "authlocal_text", "rows": "10", "button": True, "button_id": "authlocal_button",
                  "button_text": "Convert to Short Name"}




    authlocal_parsed_data = {"class": "hidden div_pad font-weight-bold", "leading_text": "Short Name",
                   "text_id": "authlocal_parsed", "name": "authlocal_parsed"}

    principal_html = pystache.render(text_template, principal_data)

    dmesg_html = pystache.render(textarea_template, authlocal_data)
    dmesg_parsed_html = pystache.render(text_template, authlocal_parsed_data)

    page_body_data = {'main_nav': main_nav_html, "body": principal_html + dmesg_html + dmesg_parsed_html,
                      "javascripts": [{"name": "authlocal.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
