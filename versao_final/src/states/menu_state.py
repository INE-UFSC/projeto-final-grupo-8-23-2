from __future__ import annotations

import pygame

import game
from states.state import State
from persistence.SingletonDAO import SingletonDAO
from states import level_state, tutorial_state, score_state
from constants import game_constants, names_musics
from utils.utils import get_file_path
from utils.buttons import text_button
from utils.images.ImageGame import ImageGame
from constants import img_names_constants

class MenuState(State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = ImageGame().transform_scale(img_names_constants.BG_MENU)
        self.__buttons = [text_button.TextButton('iniciar', 'change_to_level_state'), 
                          text_button.TextButton('tutorial', 'change_to_tutorial_state'), 
                          text_button.TextButton('placar', 'change_to_score_state'),
                          text_button.TextButton('sair', 'quit_game')]
        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 96)
        self.__font_name = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 24)
        self.__render = self.__font.render("SOUL SEEKERS", True, (255, 255, 255))
        super().__init__(game_ref, name_music=names_musics.MENU)
        self.__name = ""
        self.__nome_registrado = False
        self.__DAO = SingletonDAO.get_instance()

    def entering(self) -> None:
        super().run_bg_sound()
        self.__name = ""
        self.__nome_registrado = False

    def render(self) -> None:
        base = game_constants.SCREEN_HEIGHT / 2 - 100
        super().game_reference.screen.blit(self.__background, (0, 0))
        super().game_reference.screen.blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, base - 100))
        for button in self.__buttons:
            base += 75
            button.draw_at(super().game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base)
            if button.full_click:
                getattr(self, button.next_action)()
        
        if not self.__nome_registrado:
            base += 75
            super().game_reference.screen.blit(self.__font_name.render("Digite seu nome", True, (255, 255, 255)), ((game_constants.SCREEN_WIDTH - self.__render.get_width()/3)//2, base))
            base += 75
            super().game_reference.screen.blit(self.__font_name.render(self.__name, True, (255, 255, 255)), ((game_constants.SCREEN_WIDTH - self.__render.get_width()/3)//2, base))
        if self.__nome_registrado:
            base += 75
            super().game_reference.screen.blit(self.__font_name.render("Nome registrado com sucesso", True, (255, 255, 255)), ((game_constants.SCREEN_WIDTH - self.__render.get_width()/3)//2, base))

        super().mouse.show_mouse(super().game_reference.screen)

    def exiting(self) -> None:
        pass
    
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                self.__name += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.__name = self.__name[:-1]
                if event.key == pygame.K_RETURN:
                    self.__DAO.set_name(self.__name)
                    self.__nome_registrado = True

    def change_to_level_state(self) -> None:
        if self.__nome_registrado:
            super().game_reference.set_state(level_state.LevelState(super().game_reference))
        
    def change_to_tutorial_state(self) -> None:
        super().game_reference.set_state(tutorial_state.TutorialState(super().game_reference))

    def change_to_score_state(self) -> None:
        super().game_reference.set_state(score_state.ScoreState(super().game_reference))
        
    def quit_game(self):
        self.__DAO.dump()
        pygame.quit()
        quit()
