from helper_functions import return_form_variables

import subprocess


def return_authlocal(request):
    form = return_form_variables.return_variables(request, "principal", "authlocal")
    principal = form["principal"]
    authlocal = " ".join(form["authlocal"].splitlines())

    output = subprocess.run(["/usr/bin/java", "-classpath",
                             "/home/jphelps/webapp/auth_lib/:/home/jphelps/webapp/auth_lib/*",
                             "HadoopKerberosName",
                             authlocal, principal], stdout=subprocess.PIPE, stderr=None, encoding='utf-8')
    print(principal, authlocal)
    shortname = output.stdout
    return shortname
