import datetime
import json
import tempfile

from helper_functions import return_form_variables, return_form_files
import zipfile
import io
import csv
import getopt, sys, re, os
from xml.dom.minidom import parseString
from os.path import isfile, isdir
from subprocess import call


def return_dotpdf(request):
    form = return_form_variables.return_variables(request, "dotpdf_data")
    file_lines = form["dotpdf_data"]
    with tempfile.TemporaryDirectory(dir=os.getcwd()) as tmpdirname:

        temp_file = open(tmpdirname+"/filename.dot", 'w')
        temp_file.write(file_lines)
        temp_file.close()

        call(["dot", "-Tpdf", tmpdirname+"/filename.dot", "-o", tmpdirname + '/hive_query' + ".pdf"])
        pdf_file = open(tmpdirname+"/hive_query.pdf", 'rb').read()

    return pdf_file

