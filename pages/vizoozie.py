import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template, form_template, file_upload_template = return_template.return_templates('page.tm',
                                                                                                             'textarea.tm',
                                                                                                             'form.tm',
                                                                                                             'file_upload.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    file_upload_data = {"class": "div_pad font-weight-light", "leading_text": "Upload Oozie Workflow XML",
                        "file_upload_id": "vizoozie_fileupload", "button": True, "button_id": "upload_vizoozie_button",
                        "button_text": "Generate PDF File"}

    vizoozie_parsed_data = {"class": "font-weight-light hidden div_pad", "leading_text": "vizoozie Parsed",
                         "textarea_id": "vizoozie_parsed",
                         "name": "vizoozie_parsed", "rows": "20"}

    file_upload_html = pystache.render(file_upload_template, file_upload_data)
    vizoozie_parsed_html = pystache.render(textarea_template, vizoozie_parsed_data)

    page_body_data = {'main_nav': main_nav_html, "body": file_upload_html + vizoozie_parsed_html,
                      "javascripts": [{"name": "vizoozie.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
