# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
from raven.contrib.tornado import AsyncSentryClient
from tornado.options import (define, options, parse_command_line,
                             parse_config_file, print_help)

from .routes import routes

def main():
    define("config_dir")
    define("listen", default="0.0.0.0:80", multiple=True)

    if "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        return

    parse_command_line(final=False)

    options.run_parse_callbacks()  # same as final=True

    application = tornado.web.Application(routes, debug=bool(os.getenv("DEBUG")))
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
