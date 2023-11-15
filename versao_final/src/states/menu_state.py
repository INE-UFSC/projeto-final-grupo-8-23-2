from __future__ import annotations

import pygame

import game
from states.state import State
from states import level_state, tutorial_state
from constants import game_constants
from utils.utils import get_file_path
from utils import button, text_button


class MenuState(State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = pygame.transform.scale(pygame.image.load(f'{resources_path}/backgrounds/menu_background.jpg'),
        (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))

        self.__buttons = [text_button.TextButton('iniciar', 'level_state'), text_button.TextButton('tutorial', 'tutorial_state'), text_button.TextButton('sair', 'sair')]

        self.__play_button = self.__buttons[0]
        self.__tutorial_button = self.__buttons[1]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 96)
        self.__render = self.__font.render("SOUL SEEKERS", True, (255, 255, 255))

        path_sound = f'{get_file_path(__file__)}/sounds/game_over_menu_sound.mp3'
        super().__init__(game_ref, path_sound)

    def entering(self) -> None:
        super().run_bg_sound()

    def render(self) -> None:
        base = game_constants.SCREEN_HEIGHT / 2 - 100

        super().game_reference.screen.blit(self.__background, (0, 0))
        super().game_reference.screen.blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 100))
        for button in self.__buttons:
            base += 75
            button.draw_at(super().game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base)
                #super().game.current_state = super().game.states[button.next_state]
        super().mouse.show_mouse(super().game_reference.screen)


    def update(self) -> None: # precisamos mudar isso para nao ficar só com if
        if self.__play_button.clicked:
            super().game_reference.set_state(level_state.LevelState(super().game_reference))
            super().game_reference.set_state(level_state.LevelState(super().game_reference))
        if self.__tutorial_button.clicked:
            super().game_reference.set_state(tutorial_state.TutorialState(super().game_reference))
        if self.__buttons[2].clicked:
            pygame.quit() # achar outro jeito, assim aparece mensagem de erro

    def exiting(self) -> None:
        return super().exiting()

