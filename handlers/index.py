import tornado.web
import json
import shutil
import time
import settings

from tornado.options import options


class ViewJson(tornado.web.RequestHandler):
    def get(self):
        with open(options.filename) as data_file:
            data = json.load(data_file)

        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

        self.write(data)


class ViewEdit(tornado.web.RequestHandler):
    def get(self):
        with open("templates/edit.html",'rb') as tpl_file:
            self.write(tpl_file.read())




class CopyJson(tornado.web.RequestHandler):
    def post(self):
        # retrieve the message as json
        data = json.loads(self.request.body.decode('utf-8'))

        # first copy the file to archive
        shutil.copy2(options.filename, options.filepath + 'yleisviesti_' + time.strftime("%d%m%Y_%H%M%S") + '.json')

        # open existing file and overwrite it with new json
        with open(options.filename, 'w') as outfile:
            json.dump(data, outfile)
