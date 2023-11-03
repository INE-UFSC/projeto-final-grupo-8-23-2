from __future__ import annotations

import pygame

import game
from states.state import State
from states import level_state
from constants import game_constants
from utils.utils import get_file_path
from utils import button


class MenuState(State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = pygame.transform.scale(pygame.image.load(f'{resources_path}/backgrounds/menu_background.jpg'),
        (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))

        self.__buttons = [button.Button('iniciar', 'level_state'), button.Button('tutorial', 'tutorial'), button.Button('sair', 'sair')]

        self.__play_button = self.__buttons[0]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 96)
        self.__render = self.__font.render("SOUL SEEKERS", True, (255, 255, 255))

        path_sound = f'{get_file_path(__file__)}/sounds/menu_sound.mp3'
        super().__init__(game_ref, path_sound)

    def entering(self) -> None:
        pass

    def render(self) -> None:
        base = game_constants.SCREEN_HEIGHT / 2 - 100

        super().get_game().get_screen().blit(self.__background, (0, 0))
        super().get_game().get_screen().blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 100))
        for button in self.__buttons:
            base += 75
            if button.draw_at(super().get_game().get_screen(), (game_constants.SCREEN_WIDTH - button.width)//2, base):
                #super().game.current_state = super().game.states[button.next_state]
                pass
        super().mouse.show_mouse(super().get_game().get_screen())


    def update(self) -> None:
        if self.__play_button.get_clicked() == True:
            super().get_game().set_state(level_state.LevelState(super().get_game()))

    def exiting(self) -> None:
        return super().exiting()

