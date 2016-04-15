# -*- coding: utf-8 -*-

import os
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.autoreload
import tornado.log
import logging

# ------------------------------------------------------------------------------

def staticTemplateHandler(template):
    class GenericTemplateHandler(tornado.web.RequestHandler):
        def get(self):
            self.render(template)
    return GenericTemplateHandler

# ------------------------------------------------------------------------------

class PyGreApplication(tornado.web.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.port = kwargs.get('port', 8080)

    def start(self):
        try:
            self.listen(self.port)
            logger = logging.getLogger('tornado.general')
            logger.info('Listening on localhost:{}'.format(self.port))
            tornado.ioloop.IOLoop.current().start()
        except KeyboardInterrupt:
            logger = logging.getLogger('tornado.application')
            logger.critical('KeyboardInterrupt: Shutting down...')

# ------------------------------------------------------------------------------

def watchFiles(directory):
    for root, _, files in os.walk(directory):
        [tornado.autoreload.watch(root + '/' + f) for f in files]

# ------------------------------------------------------------------------------

def main():
    root_directory      = os.path.join(os.path.dirname(__file__))
    static_directory    = os.path.join(root_directory, 'static')
    templates_directory = os.path.join(root_directory, 'templates')
    app = PyGreApplication(
        handlers=[
            (r'/',          staticTemplateHandler('index.html')),
            (r'/register',  staticTemplateHandler('register.html')),
            (r'/contact',   staticTemplateHandler('contact.html')),
        ],
        port=8080,
        template_path=templates_directory,
        static_path=static_directory,
        debug=True,
    )

    # Remove this in production
    watchFiles(static_directory)
    watchFiles(templates_directory)
    tornado.log.enable_pretty_logging()

    app.start()

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
