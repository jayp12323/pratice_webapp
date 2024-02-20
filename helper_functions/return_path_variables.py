import json
import os

jsonpath = os.path.dirname(os.path.realpath(__file__))

paths = json.load(open(jsonpath + '/../paths.json', 'r'))


def return_variables(*args):
    path_variables = []

    for variable in args:
        try:
            path_variables.append(paths[variable])
        except:
            path_variables.append(variable + "=undefined")

    return path_variables
