from __future__ import annotations

from states.state import State
from entities import player


class LevelState(State):

    def __init__(self, game_ref) -> None:
        self.__player = player.Player()
        self.__game_ref = game_ref

    def entering(self) -> None:
        return super().entering()

    def render(self) -> None:
        self.__player.draw_at(self.__game_ref.get_screen())

    def update(self) -> None:
        return super().update()

    def exiting(self) -> None:
        return super().exiting()
