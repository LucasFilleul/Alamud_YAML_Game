# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from mud.actions import (
    GoAction, TakeAction, LookAction, InspectAction, OpenAction,
    OpenWithAction, CloseAction, TypeAction, InventoryAction, ShootAction,
    LightOnAction, LightOffAction, DropAction, DropInAction, DrinkAction, EatAction,
    PushAction, TeleportAction, EnterAction, LeaveAction, LightWithAction, PlayWithAction,
    KillAction, KillWithAction, TalkAction
)

import mud.game

def make_rules():
    GAME = mud.game.GAME
    DIRS = list(GAME.static["directions"]["noun_at_the"].values())
    DIRS.extend(GAME.static["directions"]["noun_the"].values())
    DIRS.extend(GAME.static["directions"]["normalized"].keys())
    DETS = "(?:l |le |la |les |une |un |)"

    return (
        (GoAction       , r"(?:aller |)(%s)" % "|".join(DIRS)),
        (LightWithAction, r"allumer %s(\S+) avec %s(\w+)" % (DETS,DETS)),
        (TakeAction     , r"(?:p|prendre) %s(\S+)" % DETS),
        (TalkAction     , r"(?:parler) %s(\S+)" % DETS),
        (DrinkAction    , r"(?:b|boire) %s(\S+)" % DETS),
        (EatAction      , r"(?:m|manger) %s(\S+)" % DETS),
        (LookAction     , r"(?:r|regarder)"),
        (InspectAction  , r"(?:r|regarder|lire|inspecter|observer) %s(\S+)" % DETS),
        (OpenAction     , r"ouvrir %s(\S+)" % DETS),
        (OpenWithAction , r"ouvrir %s(\S+) avec %s(\w+)" % (DETS,DETS)),
        (CloseAction    , r"fermer %s(\S+)" % DETS),
        (TypeAction     , r"(?:taper|[eé]crire) (\S+)$"),
        (InventoryAction, r"(?:inventaire|inv|i)$"),
        (LightOnAction  , r"allumer %s(\S+)" % DETS),
        (LightOffAction , r"[eé]teindre %s(\S+)" % DETS),
        (DropAction     , r"(?:poser|laisser) %s(\S+)" % DETS),
        (DropInAction   , r"(?:donner) %s(\S+) (?:a |au |)%s(\S+)" % (DETS,DETS)),
        (PushAction     , r"(?:appuyer|pousser|presser)(?: sur|) %s(\S+)" % DETS),
        (ShootAction    , r"(?:tirer|t)(?: avec|) %s(\S+)" % DETS),
        (PlayWithAction , r"jouer %s(\S+) avec %s(\w+)" % (DETS,DETS)),
        (KillAction     , r"(?:tuer|t)(?: le|) %s(\S+)" % DETS),
        (KillWithAction , r"tuer %s(\S+) avec %s(\w+)" % (DETS,DETS)),
        (TeleportAction , r"tele(?:porter|) (\S+)"),
        (EnterAction    , r"entrer"),
        (LeaveAction    , r"sortir|partir"),
    )
