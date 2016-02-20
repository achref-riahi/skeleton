# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from .handlers.hello_handler import HelloHandler

routes = [
    (r"/", HelloHandler),
]
