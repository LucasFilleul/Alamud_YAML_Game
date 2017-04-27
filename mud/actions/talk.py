# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2
from mud.events import TalkEvent

class TalkAction(Action2):
    EVENT = TalkEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "talk"
