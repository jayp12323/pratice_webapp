import pystache
from helper_functions import return_template, return_main_nav_html


def return_html():
    page_template, textarea_template, form_template, div_template = return_template.return_templates('page.tm', 'textarea.tm',
                                                                                       'form.tm', 'div.tm')
    main_nav_html = return_main_nav_html.return_main_nav_html()

    graph_data = {"class": "div_pad font-weight-light", "leading_text": "graph Text", "textarea_id": "graph_data",
                  "name": "graph_data", "rows": "10", "button": True, "button_id": "graph_button",
                  "button_text": "Graph values"}

    graph_div = {"div_id": "graph_div"}

    graph_html = pystache.render(textarea_template, graph_data)
    graph_parsed_html = pystache.render(div_template, graph_div)

    page_body_data = {'main_nav': main_nav_html, "body": graph_html + graph_parsed_html,
                      "javascripts": [{"name": "graph.js"}, {"name": "mpld3/d3.v3.min.js"},
                                      {"name": "mpld3/mpld3.v0.3.min.js"}]}
    page_html = pystache.render(page_template, page_body_data)

    return page_html
