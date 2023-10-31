from __future__ import annotations

import random

from entities import player, seeker, fight_seeker


class SeekerSpawner:
    def __init__(self, seeker_list_ref: list[seeker.Seeker], player_ref: player.Player) -> None:
        self.__seeker_list_ref = seeker_list_ref
        self.__player_ref = player_ref

    def spawn(self) -> None:
        seeker = random.choice([
            fight_seeker.FightSeeker(self.__player_ref)
        ])
        self.__seeker_list_ref.append(seeker)
