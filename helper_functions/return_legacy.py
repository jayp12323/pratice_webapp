import re
import datetime
import pendulum
from helper_functions import return_form_variables, return_form_files


def return_legacy(request, legacy_dict):
    form = return_form_variables.return_variables(request, "legacy_data")
    try:
        legacy_hortonworks_case = str(int(form["legacy_data"]))
    except ValueError:
        return "notcorrect"

    try:
        return str(legacy_dict[legacy_hortonworks_case])
    except KeyError:
        return "notfound"

