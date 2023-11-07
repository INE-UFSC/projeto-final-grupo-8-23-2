from __future__ import annotations

from states.state import State
from utils.text_button import TextButton
from constants import game_constants

import pygame
import game

class PauseState(State):
    def __init__(self, game_ref: game.Game) -> None:
        self.__buttons = [
            TextButton('continuar', 'level_state'),
            TextButton('menu', 'menu_state'),
            TextButton('sair', 'sair')
        ]
        self.__background_rect = pygame.Rect(0, 0, game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        super().__init__(game_ref)
    
    def entering(self) -> None:
        pass

    def render(self) -> None:
        height = self.__buttons[0].height
        base = (game_constants.SCREEN_HEIGHT - (height * len(self.__buttons))) / 2
        super().get_game().get_screen().fill((0, 0, 0), self.__background_rect)
        for button in self.__buttons:
            button.draw_at(super().get_game().get_screen(), (game_constants.SCREEN_WIDTH - button.width)//2, base)
            base += 75
        super().mouse.show_mouse(super().get_game().get_screen())

    def update(self) -> None:
        pass

    def exiting(self) -> None:
        pass