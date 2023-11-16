import pygame

from utils.utils import get_file_path
from utils import utils, button


class TextButton(button.Button):
    def __init__(self, text: str, state, font_size = 36) -> None:
        self.__text = text
        
        # Encontra o caminho até a pasta resources
        resources_path = get_file_path(__file__)
        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', font_size)

        self.__render = self.__font.render(self.__text, True, (utils.white))
        self.__rect = self.__render.get_rect()
        
        self.__width = self.__rect.width
        self.__height = self.__rect.height

        super().__init__(state)

    def draw_at(self, surface: pygame.Surface, x: int, y: int) -> bool:
        self.full_click = False
        self.__rect.topleft = (x, y)
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicking:
                self.clicking = True
                self.__render = self.__font.render(self.__text, True, (utils.pink))
                # depois opinem sobre esse ""
        if pygame.mouse.get_pressed()[0] == 0 and self.clicking:
            self.clicking = False
            self.full_click = True
            self.__render = self.__font.render(self.__text, True, (utils.white))
        surface.blit(self.__render, self.__rect.topleft)
    
    # Getters and Setters

    @property
    def width(self):
        return self.__width
    
    @property  
    def height(self):
        return self.__height