# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class EatEvent(Event2):
    NAME = "eat"
    def perform(self):
        if not self.object.has_prop("eatable"):
            self.fail()
            return self.inform("eat.failed")
        self.inform("eat")
