from __future__ import annotations

import pygame

import utils.utils
from entities import player
from states import state, menu_state
from constants import game_constants
from utils import mouse


class Game:
    def render(self) -> None:
        self.__current_state.render()
        pygame.display.flip()

    def run(self) -> None:

        pygame.init()
        self.__running = True
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.__mouse = mouse.Mouse()

        pygame.display.set_caption('Soul Seekers')

        self.__current_state: state.State = menu_state.MenuState(self)
        self.__current_state.entering()

        clock = pygame.time.Clock()

        while self.__running:

            self.__current_state.update()
            
            for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.__current_state.using_esc):
                    self.__running = False
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE):
                    self.__current_state.key_pressed()
            self.render()
            clock.tick(game_constants.FPS)

    def set_state(self, new_state: state.State) -> None:
        self.__current_state.exiting()
        self.__current_state = new_state
        self.__current_state.entering()
        
    @property
    def screen(self) -> pygame.Surface:
        return self.__screen