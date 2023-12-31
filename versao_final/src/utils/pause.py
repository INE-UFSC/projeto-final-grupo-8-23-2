from utils.buttons.text_button import TextButton
from constants import game_constants
import pygame

class Pause:
    def __init__(self):
        self.__buttons = [
            TextButton('continuar', 'resume_game', 42),
            TextButton('menu', 'change_to_menu', 42),
            TextButton('sair', 'quit_game', 42),
        ]
        width = game_constants.SCREEN_WIDTH // 2
        height = game_constants.SCREEN_HEIGHT // 2
        x = (game_constants.SCREEN_WIDTH - width) / 2
        y = (game_constants.SCREEN_HEIGHT - height) / 2
        
        self.__spacing = 72
        self.__bg_rect = pygame.rect.Rect(x, y, width, height)
        
    # Getters and Setters
    
    @property
    def buttons(self) -> list[TextButton]:
        return self.__buttons
    
    @property
    def bg_rect(self) -> pygame.Rect:
        return self.__bg_rect
    
    @property
    def spacing(self) -> int:
        return self.__spacing