# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class TalkEvent(Event2):
    NAME = "talk"
    def perform(self):
        if not self.object.has_prop("safe"):
            return self.talk_failed()
        else:
            self.buffer_clear()
            self.buffer_inform("talk.actor")
            self.actor.send_result(self.buffer_get())

    def talk_failed(self):
        self.fail()
        self.inform("talk.failed")
