# -*- coding: utf-8 -*-

import tornado.web
import tornado.escape
from auth import AuthHandler

# ------------------------------------------------------------------------------

class AdminHomepage(AuthHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        username = tornado.escape.xhtml_escape(self.current_user)
        print("Hello, admin user {}".format(username))
        self.render('admin-home.html', user=username)
