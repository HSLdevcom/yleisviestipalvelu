import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload

from tornado.options import define, options
from tornado.web import url

import handlers.index

define("port", default=8900, help="run on the given port", type=int)
# TODO tiedoston nimi ja archiven polku

class Application(tornado.web.Application):
    def __init__(self):
        routes = [
            url(r"/", handlers.index.ViewJson, name='index'),
            url(r"/edit", handlers.index.ViewEdit, name='muokkaa'),
            url(r"/copyJson", handlers.index.CopyJson, name='kopioi')
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )

        tornado.web.Application.__init__(self, routes, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    print("Listening on port: 8900")
    tornado.autoreload.start()

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
