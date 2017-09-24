import tornado.web
import json
import shutil
import time
import codecs

# global name variable for the main latest 'yleisviesti' file
filename = 'yleisviesti-latest.json'

class ViewJson(tornado.web.RequestHandler):
    def get(self):
        with open(filename) as data_file:
            data = json.load(data_file)

        self.write(json.dumps(data, ensure_ascii=False))

class ViewEdit(tornado.web.RequestHandler):
    def get(self):
        with open(filename) as data_file:
            data = json.load(data_file)

        self.render(
            "../templates/edit.html",
            title="Yleisviestin muokkaus",
            json=json.dumps(data)
        )

class CopyJson(tornado.web.RequestHandler):
    def post(self):
        # retrieve the message as json
        data = json.loads(self.request.body.decode('utf-8'))

        # first copy the file to archive
        shutil.copy2(filename, 'archive/yleisviesti_' + time.strftime("%d%m%Y_%H%M%S") + '.json')

        # open existing file and overwrite it with new json
        with open(filename, 'w') as outfile:
            json.dump(data, codecs.getwriter('utf-8')(outfile), ensure_ascii=False)
