import json
import shutil
import time
import re

from tornado import web
from tornado.options import options


class ViewJson(web.RequestHandler):
    def get(self):
        with open(options.filename) as data_file:
            data = json.load(data_file)
        self.write(
            re.sub(
                u'[^a-zA-Z0-9åäöÅÄÖ^_.,:;!#%&/*(){}[=?`´\'@£$€~| \-\]\"\\\n]+',
                '',
                json.dumps(
                    data,
                    indent=4,
                    ensure_ascii=False
                )
            )
        )
        self.set_header('Content-type', 'application/json')

class ViewEdit(web.RequestHandler):
    def get(self):
        with open("templates/edit.html",'rb') as tpl_file:
            self.write(tpl_file.read())

class CopyJson(web.RequestHandler):
    def post(self):
        # retrieve the message as json
        data = json.loads(
            re.sub(
                u'[^a-zA-Z0-9åäöÅÄÖ^_.,:;!#%&/*(){}[=?`´\'@£$€~| \-\]\"\\\n]+',
                '',
                self.request.body.decode('utf-8')
            )
        )

        # first copy the file to archive
        shutil.copy2(options.filename, options.filepath + 'yleisviesti_' +
                     time.strftime("%d%m%Y_%H%M%S") + '.json')

        # open existing file and overwrite it with new json
        with open(options.filename, 'w') as outfile:
            json.dump(data, outfile)
