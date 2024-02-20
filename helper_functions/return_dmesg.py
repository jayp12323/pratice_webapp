import re
import datetime
import pendulum
from helper_functions import return_form_variables, return_form_files


def return_dmesg(request, audit_data_type):
    if audit_data_type == "text":
        form = return_form_variables.return_variables(request, "dmesg_data")
        file_lines = form["dmesg_data"].splitlines()
    elif audit_data_type == "file":
        form = return_form_files.return_files(request, "dmesg_data")
        file_lines = [line.decode("utf-8") for line in form["dmesg_data"].file.read().splitlines()]

    output_lines = ""
    start_timestamp = ''
    timezone = ''

    for line in file_lines:
        if "setting system clock to" in line:
            start_time = line.split(' ')
            timezone, start_timestamp = start_time[-2:]
            start_timestamp = start_timestamp.strip('(').strip(')')

    if start_timestamp == '' or timezone == '':
        return "Starting time not found\nexiting gracefully"

    for line in file_lines:
        line_timestamp = re.sub('\[\s*', '', line).split(']')[0]
        try:
            real_time = float(start_timestamp) + float(line_timestamp)
            # print real_time
            tz = pendulum.timezone(timezone)
            dt = datetime.datetime.fromtimestamp(real_time, tz)
            output_lines += dt.strftime('%Y-%m-%d %H:%M:%S %Z%z') + " " + line + "\n"

        except:
            continue

    return output_lines
