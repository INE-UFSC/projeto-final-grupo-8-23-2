from __future__ import annotations

import pygame

import game
from states import state, menu_state
from constants import game_constants, names_musics
from utils.images.ImageGame import ImageGame
from constants import img_names_constants
from utils.utils import get_file_path
from utils.buttons import text_button
import utils.utils
from persistence.SingletonDAO import SingletonDAO
from entities import player


class GameOverState(state.State):
    def __init__(self, game_ref: game.Game, player_ref: player.Player, time_init) -> None:
        resources_path = get_file_path(__file__)
        self.__background = ImageGame().transform_scale(img_names_constants.BG_GAME_OVER)
        self.__player = player_ref
        self.__buttons = [text_button.TextButton('Voltar ao menu', 'change_to_menu_state')]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/VT323-Regular.ttf', 136)
        self.__render = self.__font.render("GAME OVER", True, utils.utils.red)
        super().__init__(game_ref, name_music=names_musics.GAME_OVER_MENU)
        self.__DAO = SingletonDAO.get_instance()
        self.__time_init = time_init

    def entering(self) -> None:
        self.run_bg_sound()
        self.__DAO.add_player(self.__player.score, ((pygame.time.get_ticks() - self.__time_init)//1000))
        self.__DAO.dump()

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