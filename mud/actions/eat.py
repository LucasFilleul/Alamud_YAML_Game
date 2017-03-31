# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2
from mud.events import EatEvent

class EatAction(Action2):
    EVENT = EatEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "eat"
