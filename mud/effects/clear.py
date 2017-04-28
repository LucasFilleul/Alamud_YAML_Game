# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .effect import Effect1
from mud.events.clear import ClearEvent

class ClearEffect(Effect1):
    EVENT = ClearEvent
