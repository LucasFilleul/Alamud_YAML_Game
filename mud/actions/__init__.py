# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .go        import GoAction, LeaveAction, EnterAction
from .inspect   import InspectAction
from .look      import LookAction
from .open      import OpenAction, OpenWithAction
from .close     import CloseAction
from .type      import TypeAction
from .take      import TakeAction
from .inventory import InventoryAction
from .light     import LightOnAction, LightOffAction, LightWithAction
from .drop      import DropAction, DropInAction
from .push      import PushAction
from .shoot     import ShootAction, ShootWithAction
from .teleport  import TeleportAction
from .drink     import DrinkAction
from .eat       import EatAction
from .jouer 	import PlayWithAction