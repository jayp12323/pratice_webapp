import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template, form_template, file_upload_template = return_template.return_templates('page.tm',
                                                                                                             'textarea.tm',
                                                                                                             'form.tm',
                                                                                                             'file_upload.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    file_upload_data = {"class": "div_pad font-weight-light", "leading_text": "Upload Revisions Zip file",
                        "file_upload_id": "revisions_fileupload", "button": True, "button_id": "upload_revisions_button",
                        "button_text": "Upload revisions File"}

    revisions_parsed_data = {"class": "font-weight-light hidden div_pad", "leading_text": "revisions Parsed",
                         "textarea_id": "revisions_parsed",
                         "name": "revisions_parsed", "rows": "20"}

    file_upload_html = pystache.render(file_upload_template, file_upload_data)
    revisions_parsed_html = pystache.render(textarea_template, revisions_parsed_data)

    page_body_data = {'main_nav': main_nav_html, "body": file_upload_html + revisions_parsed_html,
                      "javascripts": [{"name": "revisions.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
