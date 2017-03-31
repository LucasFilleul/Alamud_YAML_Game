# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import KillEvent, KillWithEvent

class ShootAction(Action2):
    EVENT = KillEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "shoot"

class ShootWithAction(Action3):
    EVENT = ShootWithEvent
    ACTION = "shoot-with"
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"