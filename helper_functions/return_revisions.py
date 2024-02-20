import datetime
import json
from helper_functions import return_form_variables, return_form_files
import zipfile
import io
import csv


def return_revisions(request, revisions_data_type):

    form = return_form_files.return_files(request, "revisions_data")
    zip_file = form["revisions_data"].file
    # if zipfile.is_zipfile(zip_file):
    output_lines = io.StringIO()
    writer = csv.writer(output_lines)
    writer.writerow(
            ["filename", "file_datetime", "attr", "configContainerType", "groupName", "hostName", "newValue",
             "oldValue", "roleName", "serviceName"])

    if zipfile.is_zipfile(zip_file):
        with zipfile.ZipFile(zip_file) as revisions_zip:
            for revisions_file in sorted(revisions_zip.namelist()):
                if "__MACOSX/"  not in revisions_file and ".json" in revisions_file:
                    file_temp = revisions_zip.open(revisions_file)
                    file_temp2=io.TextIOWrapper(file_temp,encoding='utf-8', errors='ignore').read()
                    loaded_file = json.loads(file_temp2)
                    file_timestamp = loaded_file["createdAtMillis"]
                    file_datetime = datetime.datetime.fromtimestamp(int(file_timestamp / 1000)).strftime('%Y-%m-%d %H:%M:%S')
                    configs = loaded_file["configs"]

                    for config in configs:
                        attr = config["attr"]
                        configContainerType = config["configContainerType"]
                        groupName = config["groupName"]
                        hostName = config["hostName"]
                        newValue = config["newValue"]
                        oldValue = config["oldValue"]
                        roleName = config["roleName"]
                        serviceName = config["serviceName"]

                        # Converting literal newline to escapated newline so it won't be pushed to new line in output file
                        try:
                            newValue = newValue.replace('\n', '\\n')
                        except AttributeError:
                            # New value is empty
                            pass
                        try:
                            oldValue = oldValue.replace('\n', '\\n')
                        except AttributeError:
                            # Old value is empty
                            pass
                        if attr not in ('impala_scheduled_allocations_draft','yarn_fs_scheduled_allocations_draft'):
                            writer.writerow([revisions_file, file_datetime, attr, configContainerType, groupName, hostName,
                                              newValue, oldValue, roleName, serviceName])
    return output_lines.getvalue()
