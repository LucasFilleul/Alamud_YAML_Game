# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2, Event3

class KillEvent(Event2):
    NAME = "kill"
    def perform(self):
        if not self.object.has_prop("killable"):
            self.fail()
            return self.inform("kill.failed")
        self.inform("kill")

class KillWithEvent(Event3):
    NAME = "kill-with"
    def perform(self):
        if not self.object.has_prop("killable-with") or not self.object2.has_prop("shootable"):
            self.fail()
            return self.inform("kill-with.failed")
        self.inform("kill-with")