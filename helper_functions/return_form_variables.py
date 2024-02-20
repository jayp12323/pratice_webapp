def return_variables(request, *args):
    form_variables = {}
    for variable in args:
        try:
            if "[]" in variable:
                variable_array = request.forms.getall(variable)
                form_variables[variable] = [x.strip() for x in variable_array]

            else:
                form_variables[variable] = request.forms.get(variable).strip()
        except:
            form_variables[variable] = None

    return form_variables
