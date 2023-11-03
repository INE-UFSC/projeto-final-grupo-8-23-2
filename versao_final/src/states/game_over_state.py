from __future__ import annotations

import pygame

import game
from states import state, menu_state
from constants import game_constants
from utils.utils import get_file_path
from utils import button


class GameOverState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = pygame.transform.scale(pygame.image.load(f'{resources_path}/backgrounds/bg_game_over_2.jpg'),
        (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))

        self.__buttons = [button.Button('Voltar ao menu', 'menu_state')]

        self.__back_to_menu_button = self.__buttons[0]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/Kemco Pixel Bold.ttf', 96)
        self.__render = self.__font.render("GAME OVER", True, (255, 0, 0))
        path_sound = f'{get_file_path(__file__)}/sounds/game_over_menu_sound.mp3'
        super().__init__(game_ref, path_sound)

    def entering(self) -> None:
        pass

    def render(self) -> None:
        base = game_constants.SCREEN_HEIGHT / 2 - 10

        super().get_game().get_screen().blit(self.__background, (0, 0))
        super().get_game().get_screen().blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 40))
        for button in self.__buttons:
            base += 75
            if button.draw_at(super().get_game().get_screen(), (game_constants.SCREEN_WIDTH - button.width)//2, base):
                #super().game.current_state = super().game.states[button.next_state]
                pass
        super().mouse.show_mouse(super().get_game().get_screen())


    def update(self) -> None:
        if self.__back_to_menu_button.get_clicked():
            super().get_game().set_state(menu_state.MenuState(super().get_game()))
        pass

    def exiting(self) -> None:
        return super().exiting()

