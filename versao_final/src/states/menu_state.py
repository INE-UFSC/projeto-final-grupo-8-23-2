from __future__ import annotations

import pygame

import game
from states.state import State
from constants import game_constants
from utils import button


class MenuState(State):
    def __init__(self, game_ref: game.Game) -> None:
        self.__background = pygame.transform.scale(pygame.image.load('versao_final/resources/menubackground.jpg'),
                                                   (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        self.__buttons = [button.Button('iniciar', 'level_state'), button.Button('tutorial', 'tutorial'), button.Button('sair', 'sair')]
        self.__font = pygame.font.Font('versao_final/resources/NightsideDemoRegular.ttf', 96)
        self.__render = self.__font.render("SOUL SEEKERS", True, (255, 255, 255))
        super().__init__(game_ref)

    def entering(self) -> None:
        pass

    def render(self) -> None:
        base = game_constants.SCREEN_HEIGHT / 2 - 100
        self.draw_background(super().get_game().get_screen())
        super().get_game().get_screen().blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 100))
        for button in self.__buttons:
            base += 75
            if button.draw_at(super().get_game().get_screen(), (game_constants.SCREEN_WIDTH - button.width)//2, base):
                super().game.current_state = super().game.states[button.next_state]
        super().mouse.show_mouse(super().get_game().get_screen())
        

    def update(self) -> None:
        pass

    def exiting(self) -> None:
        return super().exiting()

    def draw_background(self, screen):
        screen.blit(self.__background, (0, 0))