# -*- coding: utf-8 *-*
import logging
import tornado.web
import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.options import define, options

from testexample.example_app import ExampleApp

if __name__ == '__main__':
    define('port', default='8080', help='port number')
    app = ExampleApp()
    app.listen(options.port)
    logging.info('Listening on port %s' % options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
