# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event1

class ClearEvent(Event1):
    NAME = "clear"

    def perform(self):
        self.inform("clear")
        cont = self.actor.container()
        for x in list(self.actor.contents()):
            x.move_to(cont)

