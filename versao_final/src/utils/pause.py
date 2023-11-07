from utils.text_button import TextButton
from constants import game_constants
import pygame

class Pause:
    def __init__(self):
        self.__buttons = [
            TextButton('continuar', 'level_state', 30),
            TextButton('menu', 'menu_state', 30),
            TextButton('sair', 'sair', 30)
        ]
        width = game_constants.SCREEN_WIDTH // 2
        height = game_constants.SCREEN_HEIGHT // 2
        x = (game_constants.SCREEN_WIDTH - width) / 2
        y = (game_constants.SCREEN_HEIGHT - height) / 2
        
        self.__spacing = 50
        self.__bg_rect = pygame.rect.Rect(x, y, width, height)
    
    @property
    def buttons(self) -> list[TextButton]:
        return self.__buttons
    
    @property
    def bg_rect(self) -> pygame.Rect:
        return self.__bg_rect
    
    @property
    def spacing(self) -> int:
        return self.__spacing