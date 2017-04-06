# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class ShootEvent(Event2):
    NAME = "shoot"
    def perform(self):
        if not self.object.has_prop("shootable"):
            self.fail()
            return self.inform("shoot.failed")
        self.inform("shoot")
