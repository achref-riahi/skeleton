# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import sys

import tornado.ioloop
from tornado.options import options, define, print_help, parse_command_line, parse_config_file
import tornado.web
import tornado.httpserver

from .routes import routes


def main():
    define("config_dir")
    define("listen", default="0.0.0.0:80", multiple=True)

    if "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        return

    parse_command_line(final=False)

    application = tornado.web.Application(routes)
    server = tornado.httpserver.HTTPServer(application)
    for addr in options.listen:
        port = 80
        address = addr
        try:
            address, port = addr.rsplit(':', 1)
            port = int(port)
        except ValueError:
            pass
        server.listen(port, address=address)
    tornado.ioloop.IOLoop.instance().start()
