from __future__ import annotations

import pygame

import game
from states import state, menu_state
from constants import game_constants
from utils.utils import get_file_path
from utils.buttons import text_button
import utils.utils


class GameOverState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = pygame.transform.scale(pygame.image.load(f'{resources_path}/backgrounds/bg_game_over_2.jpg'),
        (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))

        self.__buttons = [text_button.TextButton('Voltar ao menu', 'change_to_menu_state')]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/VT323-Regular.ttf', 136)
        self.__render = self.__font.render("GAME OVER", True, utils.utils.red)
        path_sound = f'{get_file_path(__file__)}/sounds/menu_sound.mp3'
        super().__init__(game_ref, path_sound, volumn_sound=0.4)

    def entering(self) -> None:
        self.run_bg_sound()

    def render(self) -> None:
        base = game_constants.SCREEN_HEIGHT / 2 - 10

        super().game_reference.screen.blit(self.__background, (0, 0))
        super().game_reference.screen.blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 80))
        for button in self.__buttons:
            base += 75
            button.draw_at(self.game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base)
            if button.full_click:
                getattr(self, button.next_action, None)()
        super().mouse.show_mouse(super().game_reference.screen)

    def update(self) -> None:
        pass

    def exiting(self) -> None:
        return super().exiting()

    def change_to_menu_state(self):
        super().game_reference.set_state(menu_state.MenuState(self.game_reference))