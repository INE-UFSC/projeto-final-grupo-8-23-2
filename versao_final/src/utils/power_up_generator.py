from __future__ import annotations

import random

from powerups import power_up, power_up_health, power_up_speed
from entities import player


class PowerUpGenerator:
    def __init__(self, power_up_list_ref: list[power_up.PowerUp], player_ref: player.Player) -> None:
        self.__power_ups = power_up_list_ref
        self.__player = player_ref

    def generate(self) -> None:
        power_up = random.choice([
            power_up_health.PowerUpHealth(self.__player),
            power_up_speed.PowerUpSpeed(self.__player)
        ])
        self.__power_ups.append(power_up)

