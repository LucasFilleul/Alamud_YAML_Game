# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class GiveEvent(Event2):
    NAME = "give"
    def perform(self):
        if not self.object.has_prop("givable"):
            self.fail()
            return self.inform("give.failed")
        self.inform("give")
