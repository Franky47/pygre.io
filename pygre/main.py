# -*- coding: utf-8 -*-

import os
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.autoreload
import tornado.log
import tornado.escape
import logging
from auth   import LoginHandler, LogoutHandler
from admin  import AdminHomepage

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

    # Define & parse command line options
    tornado.options.define('debug', default=False, help='Enable Debug mode')
    tornado.options.define('cookie_secret', default='', help='Secret for encypting cookies')
    tornado.options.define('port', default=8080, help='Listening port')
    tornado.options.parse_command_line()

    app = PyGreApplication(
        handlers=[
            # Static pages
            (r'/',          staticTemplateHandler('index.html')),
            (r'/register',  staticTemplateHandler('register.html')),
            (r'/contact',   staticTemplateHandler('contact.html')),

            # User management
            (r'/login',     LoginHandler),
            (r'/logout',    LogoutHandler),

            # Admin section
            (r'/admin',     AdminHomepage),
        ],
        template_path=templates_directory,
        static_path=static_directory,
        **tornado.options.options.as_dict()
    )

    if tornado.options.options.debug:
        watchFiles(static_directory)
        watchFiles(templates_directory)
        tornado.log.enable_pretty_logging()

    app.start()

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
