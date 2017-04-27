# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2
from mud.events import GiveEvent

class GiveAction(Action2):
    EVENT = GiveEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "give"
