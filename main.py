from __future__ import print_function
from os.path import dirname, join
import handlers.index
import settings  # pylint: disable=unused-import

from tornado import autoreload, httpserver, ioloop, web
from tornado.options import options
from tornado.web import url


class Application(web.Application):
    def __init__(self):
        routes = [
            url(r"/", handlers.index.ViewJson, name='index'),
            url(r"/edit", handlers.index.ViewEdit, name='muokkaa'),
            url(r"/copyJson", handlers.index.CopyJson, name='kopioi')
        ]

        config = dict(
            template_path=join(dirname(__file__), "templates"),
            static_path=join(dirname(__file__), "static")
        )

        web.Application.__init__(self, routes, **config)


def main():
    options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    print("Listening on port: " + str(options.port))
    autoreload.start()

    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
