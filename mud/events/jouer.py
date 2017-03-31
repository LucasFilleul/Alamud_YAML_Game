# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2, Event3

class PlayWithEvent(Event3):
    NAME = "play-with"

    def perform(self):
        if not self.object.has_prop("jouable-with") and not self.object2.has_prop("jouable-with"):
            self.fail()
            return self.inform("jouable-with.failed")
        self.inform("jouable-with")
