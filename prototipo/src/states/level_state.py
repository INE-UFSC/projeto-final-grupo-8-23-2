from __future__ import annotations

from states.state import State
from entities import player
from entities import seeker, fight_seeker
from powerups import power_up, power_up_health
import math

class LevelState(State):
    def __init__(self, game_ref) -> None:
        self.__game_ref = game_ref
        self.__player: player.Player = player.Player()
        self.__seekers: list[seeker.Seeker] = [fight_seeker.FightSeeker(self.__player) for _ in range(2)]
        self.__power_ups: list[power_up.PowerUp] = [power_up_health.PowerUpHealth(self.__player) for _ in range(2)]

    def entering(self) -> None:
        return super().entering()

    def render(self) -> None:
        self.__player.draw_at(self.__game_ref.get_screen())
        self.__player.move()
        self.__player.get_power_up()
        for seeker in self.__seekers:
            seeker.draw_at(self.__game_ref.get_screen())
            seeker.move()
        for powerup in self.__power_ups:
            powerup.draw_at(self.__game_ref.get_screen())
            powerup.add_power_up_to_list()

    def update(self) -> None:
        return super().update()

    def exiting(self) -> None:
        return super().exiting()
