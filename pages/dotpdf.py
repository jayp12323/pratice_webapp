import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template,div_template, form_template, file_upload_template = return_template.return_templates('page.tm',
                                                                                                             'textarea.tm',
                                                                                                             'div.tm',
                                                                                                             'form.tm',
                                                                                                             'file_upload.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    dotpdf_data = {"class": "div_pad font-weight-light", "leading_text": "dotpdf Text", "textarea_id": "dotpdf_text",
                  "name": "dotpdf_text", "rows": "10", "button": True, "button_id": "dotpdf_button",
                  "button_text": "Convert Dot to PDF"}

    dotpdf_parsed_data = {"class": " div_pad",
                         "div_id": "dotpdf_pdf",
                         "name": "dotpdf_pdf"}

    file_upload_html = pystache.render(textarea_template, dotpdf_data)
    dotpdf_parsed_html = pystache.render(div_template, dotpdf_parsed_data)

    page_body_data = {'main_nav': main_nav_html, "body": file_upload_html + dotpdf_parsed_html,
                      "javascripts": [{"name": "dotpdf.js"},{"name": "pdfobject.min.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
