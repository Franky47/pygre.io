# -*- coding: utf-8 -*-

import tornado.web
import tornado.escape

# ------------------------------------------------------------------------------

class AuthHandler(tornado.web.RequestHandler):
    def get_login_url(self):
        return '/login'

    def get_current_user(self):
        user = self.get_secure_cookie('user')
        if user:
            return tornado.escape.json_decode(user)
        else:
            return None

# --

class LoginHandler(AuthHandler):
    def get(self, *args, **kwargs):
        errormessage = self.get_argument('error', '')
        next = self.get_argument('next', '/')
        self.render('login.html',
                    errormessage=errormessage,
                    post_url='/login?next={}'.format(tornado.escape.url_escape(next)))

    def post(self, *args, **kwargs):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        auth = self._check_permission(password, username)
        if auth:
            self._set_current_user(username)
            next = self.get_argument('next', '/')
            self.redirect(next)
        else:
            error_msg = '?error=' + tornado.escape.url_escape('Login incorrect')
            self.redirect('/login' + error_msg)

    # --

    def _check_permission(self, password, username):
        # Dumbest security ever.
        if username == 'admin' and password == 'password':
            return True
        return False

    def _set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie('user')

# --

class LogoutHandler(AuthHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('user')
        self.redirect(self.get_argument('next', '/'))
