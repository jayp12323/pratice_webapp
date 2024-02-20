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


def return_vizoozie(request):

    form = return_form_files.return_files(request, "vizoozie_data")
    file_lines = form["vizoozie_data"]
    filename = file_lines.filename

    vizoozie = VizOozie()
    pdf_file = vizoozie.processWorkflow(file_lines.file, filename, "")
    return pdf_file

def sText(text):
    return text.replace('-', '_')


class VizOozie(object):
    properties = {}
    def getName(self, node):
        attr = self.getAttribute(node, "name")
        return attr

    def getTo(self, node):
        attr = self.getAttribute(node, "to")
        return attr

    def getAttribute(self, node, attributeName):
        attr = node.getAttribute(attributeName)
        return attr

    def getOK(self, node):
        ok = node.getElementsByTagName("ok")[0]
        return ok

    def getError(self, node):
        return node.getElementsByTagName("error")[0]

    def getOKTo(self, node):
        return self.getTo(self.getOK(node))

    def getErrorTo(self, node):
        return self.getTo(self.getError(node))

    def processHeader(self, name):
        output = "digraph{\nsize = \"8,8\";ratio=fill;node[fontsize=24];labelloc=\"t\";label=\"" + name + "\";\nsubgraph{\n"
        return output

    def processStart(self, doc):
        output = ''
        start = doc.getElementsByTagName("start")[0]
        to = self.getTo(start)
        output = '\n' + "start -> " + to.replace('-', '_') + ";\n"
        return output

    def getFirstElementChildNode(self, node):
        for aNode in node.childNodes:
            if aNode.nodeType == aNode.ELEMENT_NODE:
                return aNode
        return None

    def processAction(self, doc):
        output = ''
        for node in doc.getElementsByTagName("action"):
            name = self.getName(node)
            action_node = self.getFirstElementChildNode(node)
            color = "white"
            if action_node.tagName == "sub-workflow":
                url = self.getFirstElementChildNode(action_node).childNodes[0].data
                url = url.replace("${subworkflowPath}", "")
                url = re.sub('.xml$', '.svg', url)
                output += '\n' + sText(name) + " [URL=\"" + url + "\",shape=box,style=filled,color=" + color + "];\n"
            else:
                output += '\n' + sText(name) + " [shape=box,style=filled,color=" + color + "];\n"
            output += '\n' + sText(name) + " -> " + sText(self.getOKTo(node)) + ";\n"
            output += '\n' + sText(name) + " -> " + sText(self.getErrorTo(node)) + "[style=dotted,fontsize=10];\n"
        return output

    def processFork(self, doc):
        output = ''
        for node in doc.getElementsByTagName("fork"):
            name = self.getName(node)
            output += '\n' + name.replace('-', '_') + " [shape=octagon];\n"
            for path in node.getElementsByTagName("path"):
                start = path.getAttribute("start")
                output += '\n' + name.replace('-', '_') + " -> " + start.replace('-', '_') + ";\n"
        return output

    def processJoin(self, doc):
        output = ''
        for node in doc.getElementsByTagName("join"):
            name = self.getName(node)
            to = self.getTo(node)
            output += '\n' + name.replace('-', '_') + " [shape=octagon];\n"
            output += '\n' + name.replace('-', '_') + " -> " + to.replace('-', '_') + ";\n"
        return output

    def processDecision(self, doc):
        output = ''
        for node in doc.getElementsByTagName("decision"):
            name = self.getName(node)
            switch = node.getElementsByTagName("switch")[0]
            output += '\n' + name.replace('-', '_') + " [shape=diamond];\n"
            for case in switch.getElementsByTagName("case"):
                to = case.getAttribute("to")
                caseValue = case.childNodes[0].nodeValue.replace('"', '')
                output += '\n' + name.replace('-', '_') + " -> " + to.replace('-', '_') + "[style=bold,fontsize=20];\n"

            default = switch.getElementsByTagName("default")[0]
            to = default.getAttribute("to")
            output += '\n' + name.replace('-', '_') + " -> " + to.replace('-', '_') + "[style=dotted,fontsize=20];\n"
        return output

    def processCloseTag(self):
        output = '\n' + "}" + '\n' + "}"
        return output

    def convertWorkflowXMLToDOT(self, input_str, name=""):
        doc = parseString(input_str)

        if doc.getElementsByTagName("workflow-app").length == 0: return None

        output = self.processHeader(name)
        output += self.processStart(doc)
        output += self.processAction(doc)
        output += self.processFork(doc)
        output += self.processJoin(doc)
        output += self.processDecision(doc)
        output += self.processCloseTag()
        return output

    def processWorkflow(self, in_file, out_file, relative_name):
        input_str = in_file.read()
        output = self.convertWorkflowXMLToDOT(input_str, relative_name)
        print(os.path.splitext(out_file)[0])
        temp_file = open("filename.dot",'w')
        temp_file.write(output)
        temp_file.close()

        print(["dot", "-Tpdf", "filename.dot", "-o", os.getcwd()+'/'+os.path.splitext(out_file)[0] + ".pdf"])
        call(["dot", "-Tpdf", "filename.dot", "-o", os.getcwd()+'/'+os.path.splitext(out_file)[0] + ".pdf"])
        pdf_file = open(os.path.splitext(out_file)[0] + ".pdf",'rb').read()
        return pdf_file

