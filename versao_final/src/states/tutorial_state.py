from __future__ import annotations

import pygame

import game
from states import state, menu_state
from constants import game_constants, names_musics
from utils.utils import get_file_path
from utils.buttons import text_button
from utils.images.ImageGame import ImageGame
from constants import img_names_constants
class TutorialState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        resources_path = get_file_path(__file__)
        self.__background = ImageGame().transform_scale(img_names_constants.BG_TUTORIAL)
        
        self.__tutorial_img = ImageGame().transform_scale_2x(img_names_constants.TUTORIAL_MODAL)
        self.__buttons = [text_button.TextButton('Voltar ao menu', 'change_to_menu_state')]
        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 64)
        self.__render = self.__font.render("Tutorial", True, (255, 255, 255))
        super().__init__(game_ref, name_music=names_musics.TUTORIAL, using_esc=True)

    def entering(self) -> None:
        super().run_bg_sound()

    def render(self) -> None:
        
        # mostra o background
        super().game_reference.screen.blit(self.__background, (0, 0)) 
        
        # mostra o titulo
        super().game_reference.screen.blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, 50)) 
        
        # mostra a imagem do tutorial
        super().game_reference.screen.blit(self.__tutorial_img, ( 
                                           (game_constants.SCREEN_WIDTH - self.__tutorial_img.get_width())//2, 
                                           (game_constants.SCREEN_HEIGHT - self.__tutorial_img.get_height())//2 + 20))
        
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

