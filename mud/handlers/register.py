# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

import tornado.escape
from mud.handlers.base import BaseHandler
from mud.db.user import DATABASE as USERS

#==============================================================================
# the registration handler also uses the user db
#==============================================================================

class RegisterHandler(BaseHandler):

    def extras(self):
        return {
            "next"                  : self.get_argument("next", "/"),
            "password_mismatch"     : False,
            "username_not_available": False,
            "username_empty"        : False,
            "password_empty"        : False,
        }

    def get(self):
        self.render("register.html", **self.extras())

    def post(self):
        username  = self.get_argument("username", "")
        password1 = self.get_argument("password1", "")
        password2 = self.get_argument("password2", "")
        extras    = self.extras()
        if not username:
            extras["username_empty"] = True
        elif password1!=password2:
            extras["password_mismatch"] = True
        elif not password1:
            extras["password_empty"] = True
        else:
            avail = USERS.create_user(username, password1)
            if avail:
                self.set_secure_cookie(
                    "mud_player", tornado.escape.json_encode(username))
                self.redirect(extras["next"])
                return
            extras["username_not_available"] = True
        self.render("register.html", **extras)