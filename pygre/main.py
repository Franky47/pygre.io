# -*- coding: utf-8 -*-

import os
import tornado.web
import tornado.ioloop
import tornado.options

# ------------------------------------------------------------------------------

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')

# ------------------------------------------------------------------------------

class PyGreApplication(tornado.web.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.port = kwargs.get('port', 8080)

    def start(self):
        try:
            self.listen(self.port)
            print('Listening on localhost:{}'.format(self.port))
            tornado.ioloop.IOLoop.current().start()
        except KeyboardInterrupt:
            print('KeyboardInterrupt: Shutting down...')

# ------------------------------------------------------------------------------

def main():
    root_directory = os.path.join(os.path.dirname(__file__))
    app = PyGreApplication(
        handlers=[
            # Handlers go here
            (r'/',          IndexHandler),
            (r'/register',  RegisterHandler),
        ],
        port=8080,
        template_path=os.path.join(root_directory, 'templates'),
        static_path=os.path.join(root_directory, 'static'),
        debug=True,
    )
    app.start()

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
