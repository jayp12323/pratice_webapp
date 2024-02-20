from helper_functions import return_path_variables

rootpath = return_path_variables.return_variables("webapp_root_path")[0]


def return_templates(*args):
    templates = []

    for template in args:
        templates.append(open(rootpath + '\\templates\\' + template, 'r').read())
    return templates
