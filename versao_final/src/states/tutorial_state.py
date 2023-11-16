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
        self.__background = pygame.transform.scale(pygame.image.load(f'{resources_path}/backgrounds/tutorial_bg.jpg'),
                                                    (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        
        self.__tutorial_img = pygame.transform.scale2x(pygame.image.load(f'{resources_path}/backgrounds/tutorial.png')),

        self.__buttons = [text_button.TextButton('Voltar ao menu', menu_state.MenuState(game_ref))]

        self.__back_to_menu_button = self.__buttons[0]

        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 64)
        self.__render = self.__font.render("Tutorial", True, (255, 255, 255))
        path_sound = f'{get_file_path(__file__)}/sounds/tutorial_sound.mp3'
        super().__init__(game_ref, path_sound, volumn_sound=0.4, using_esc=True)

    def entering(self) -> None:
        super().run_bg_sound()

    def render(self) -> None:
        
        # mostra o background
        super().game_reference.screen.blit(self.__background, (0, 0)) 
        
        # mostra o titulo
        super().game_reference.screen.blit(self.__render, ((game_constants.SCREEN_WIDTH - self.__render.get_width())//2, 50)) 
        
        # mostra a imagem do tutorial
        super().game_reference.screen.blit(self.__tutorial_img[0], ( ## por alguma razao to tendo que botar um [0], alguem sabe?
                                           (game_constants.SCREEN_WIDTH - self.__tutorial_img[0].get_width())//2, 
                                           (game_constants.SCREEN_HEIGHT - self.__tutorial_img[0].get_height())//2 + 20))
        
        base = game_constants.SCREEN_HEIGHT - 50 - self.__buttons[0].height
        # mostra os botoes
        for button in self.__buttons:
            base += 10
            if button.draw_at(super().game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base):
                #super().game.current_state = super().game.states[button.next_state]
                pass
        
        
        super().mouse.show_mouse(super().game_reference.screen)

    def update(self) -> None:
        if self.__back_to_menu_button.full_click:
            super().game_reference.set_state(menu_state.MenuState(super().game_reference))

    def exiting(self) -> None:
        return super().exiting()
    
    def key_pressed(self) -> None:
        super().game_reference.set_state(menu_state.MenuState(super().game_reference))

