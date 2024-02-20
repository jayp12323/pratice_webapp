#!/usr/bin/env python

import matplotlib.pyplot as plt, mpld3
from helper_functions import return_form_variables


def return_graph(request):
    form = return_form_variables.return_variables(request, "graph_data")

    file_lines = form["graph_data"].splitlines()
    lines = []
    for line in file_lines:
        clean_line = line.strip()
        if not clean_line:
            # skip empty lines (ie: newlines)
            continue
        if clean_line[0] in ['"', "'"]:
            clean_line = clean_line.strip("\"'")
        lines.append(int(clean_line))

    fig, ax = plt.subplots()
    plt.rc('axes', labelsize=14)
    ax.plot(file_lines)
    return mpld3.fig_to_html(fig)

