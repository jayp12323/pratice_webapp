def return_files(request, *args):
    form_files = {}
    for file in args:
        try:
            if "[]" in file:
                file_array = request.files.getall(file)
                form_files[file] = [x for x in file_array]

            else:
                form_files[file] = request.files.get(file)
        except:
            form_files[file] = None

    return form_files
