import datetime
import json
from helper_functions import return_form_variables, return_form_files


def return_audit(request, audit_data_type):

    if audit_data_type == "text":
        form = return_form_variables.return_variables(request, "audit_data")
        file_lines = form["audit_data"].splitlines()
    elif audit_data_type == "file":
        form = return_form_files.return_files(request, "audit_data")
        file_lines = [line.decode("utf-8") for line in form["audit_data"].file.read().splitlines()]

    output_lines = ""
    for line in file_lines:
        try:
            json_line = json.loads(line.strip())
        except:
            continue
        json_line["eventTime"] = datetime.datetime.fromtimestamp(
            float(int(json_line["eventTime"]) / 1000)).strftime('%Y-%m-%d %H:%M:%S')
        output_lines += json.dumps(json_line) + "\n"

    return output_lines
