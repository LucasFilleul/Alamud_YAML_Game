# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import KillEvent, KillWithEvent

class KillAction(Action2):
    EVENT = KillEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "kill"

class KillWithAction(Action3):
    EVENT = KillWithEvent
    ACTION = "kill-with"
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"