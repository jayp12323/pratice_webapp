import os

from bottle import BaseRequest, run, route, static_file, request, response,default_app
from gevent import monkey
import wsgigzip
import json

rootpath = os.path.dirname(os.path.realpath(__file__))
hostname = "localhost"

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=rootpath + '/static')

@route('')
@route('/')
@route('/dash')
@route('/dash/')
def start():
    from pages.dash import return_html
    return return_html()


if __name__ == "__main__":
    monkey.patch_all()
    BaseRequest.MEMFILE_MAX = 1024 * 1024
    application = wsgigzip.GzipMiddleware(default_app())
    run(application, host=hostname, port=28080, server='gevent')
