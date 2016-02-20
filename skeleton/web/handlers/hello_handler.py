# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import tornado.web


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
