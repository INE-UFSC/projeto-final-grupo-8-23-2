from __future__ import annotations

import pygame

import game
from states import state, menu_state
from constants import game_constants
from utils.utils import get_file_path
from utils import text_button


class TutorialState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = pygame.transform.scale(pygame.image.load(f'{resources_path}/backgrounds/tutorial_page_2.png'),
        (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))

        self.__buttons = [text_button.TextButton('Voltar ao menu', menu_state.MenuState(game_ref))]

        self.__back_to_menu_button = self.__buttons[0]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/Kemco Pixel Bold.ttf', 96)
        self.__render = self.__font.render("", True, (255, 0, 0))
        path_sound = f'{get_file_path(__file__)}/sounds/tutorial_sound.mp3'
        super().__init__(game_ref, path_sound, volumn_sound=0.4)

    def entering(self) -> None:
        super().run_bg_sound()

    def render(self) -> None:
        base = 0
        super().get_game().get_screen().blit(self.__background, (0, 0))
        super().get_game().get_screen().blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 40))
        for button in self.__buttons:
            base += 10
            if button.draw_at(super().get_game().get_screen(), (game_constants.SCREEN_WIDTH - button.width)//2, base):
                #super().game.current_state = super().game.states[button.next_state]
                pass
        super().mouse.show_mouse(super().get_game().get_screen())

    def update(self) -> None:
        if self.__back_to_menu_button.clicked:
            super().get_game().set_state(menu_state.MenuState(super().get_game()))
        pass

    def exiting(self) -> None:
        return super().exiting()

