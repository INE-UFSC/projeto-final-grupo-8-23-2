from __future__ import annotations

from states.state import State
from entities import player
from entities import seeker, fight_seeker
import math

class LevelState(State):
    def __init__(self, game_ref) -> None:
        self.__game_ref = game_ref
        self.__player: player.Player = player.Player()
        self.__seekers: list[seeker.Seeker] = [fight_seeker.FightSeeker(self.__player) for _ in range(10)]

    def entering(self) -> None:
        return super().entering()

    def render(self) -> None:
        self.__player.draw_at(self.__game_ref.get_screen())
        self.__player.move()
        for i in range(len(self.__seekers)):
            next_seeker = None
            seeker = self.__seekers[i]
            if i < (len(self.__seekers) - 2):
                next_seeker = self.__seekers[i+1]
            if next_seeker != None:
                seeker.distance_between_seeker(next_seeker)
            seeker.draw_at(self.__game_ref.get_screen())
            seeker.move()

    def update(self) -> None:
        return super().update()

    def exiting(self) -> None:
        return super().exiting()
