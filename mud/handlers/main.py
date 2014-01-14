# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from mud.handlers.base import BaseHandler
from mud.db.transcript import DATABASE as TRANSCRIPTS

#==============================================================================
# home page of the mud and also play page when the user is logged in.
#==============================================================================

class MainHandler(BaseHandler):

    def get(self):
        if self.get_current_user():
            self.render("play.html", **self.extras())
        else:
            self.render("index.html")

    def extras(self):
        return {
            "messages": TRANSCRIPTS.lookup(self.get_current_user())
        }

    @tornado.web.authenticated
    def post(self):
        user = self.get_current_user()
        command = self.get_argument("command")