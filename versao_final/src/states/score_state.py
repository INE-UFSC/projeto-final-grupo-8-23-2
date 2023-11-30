from __future__ import annotations

import pygame

import game
from states import state, menu_state
from constants import game_constants, names_musics
from utils.utils import get_file_path
from utils.buttons import text_button
from utils.images.ImageGame import ImageGame
from constants import img_names_constants
from persistence.SingletonDAO import SingletonDAO


class ScoreState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = ImageGame().transform_scale(img_names_constants.BG_TUTORIAL)
        
        self.__tutorial_img = ImageGame().transform_scale_2x(img_names_constants.TUTORIAL_MODAL)
        self.__buttons = [text_button.TextButton('Voltar ao menu', 'change_to_menu_state')]
        self.__font = pygame.font.Font(f'{resources_path}/fonts/ARCADECLASSIC.TTF', 40)
        self.__font2 = pygame.font.Font(f'{resources_path}/fonts/ARCADECLASSIC.TTF', 35)
        self.__font3 = pygame.font.Font(f'{resources_path}/fonts/ARCADECLASSIC.TTF', 30)
        self.__render = self.__font.render("Placar", True, (255, 255, 255))
        self.__render2 = self.__font.render("Nome     Pontuacao     Tempo(s)", True, (255, 255, 255))
        super().__init__(game_ref, name_music=names_musics.TUTORIAL, using_esc=True)

        self.__DAO = SingletonDAO.get_instance()

    def entering(self) -> None:
        super().run_bg_sound()

    def render(self) -> None:
        
        # mostra o background
        super().game_reference.screen.blit(self.__background, (0, 0)) 
        
        # mostra o titulo
        super().game_reference.screen.blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, 50))

        # mostra o subtitulo
        super().game_reference.screen.blit(self.__render2, ((game_constants.SCREEN_WIDTH - self.__render2.get_width())//2, 100)) 
        
        # mostra o placar
        i = 0
        for elements in zip(self.__DAO.get_players_name(), self.__DAO.get_players_score(), self.__DAO.get_players_time()):
            self.__nome = self.__font3.render(elements[0], True, (255, 255, 255))
            self.__pontuacao = self.__font3.render(str(elements[1]), True, (255, 255, 255))
            self.__tempo = self.__font3.render(str(elements[2]), True, (255, 255, 255))
            super().game_reference.screen.blit(self.__nome, ((game_constants.SCREEN_WIDTH - self.__nome.get_width())//2 - 100, 150+i))
            super().game_reference.screen.blit(self.__pontuacao, ((game_constants.SCREEN_WIDTH - self.__pontuacao.get_width())//2, 150+i))
            super().game_reference.screen.blit(self.__tempo, ((game_constants.SCREEN_WIDTH - self.__tempo.get_width())//2 + 100, 150+i))
            i += 50


        
        base = game_constants.SCREEN_HEIGHT - 50 - self.__buttons[0].height
        # mostra os botoes
        for button in self.__buttons:
            base += 10
            button.draw_at(super().game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base)
            if button.full_click:
                getattr(self, button.next_action, None)()
        
        super().mouse.show_mouse(super().game_reference.screen)
        
        # Functions
    
    def change_to_menu_state(self):
        super().game_reference.set_state(menu_state.MenuState(self.game_reference))

    def update(self) -> None:
        pass

    def exiting(self) -> None:
        return super().exiting()
    
    def key_pressed(self) -> None:
        super().game_reference.set_state(menu_state.MenuState(super().game_reference))

