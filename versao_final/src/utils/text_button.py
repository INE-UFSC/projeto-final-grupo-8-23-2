import pygame

from utils.utils import get_file_path
from utils import utils, button


class TextButton(button.Button):
    def __init__(self, text: str, state) -> None:
        self.__text = text
        
        # Encontra o caminho até a pasta resources
        resources_path = get_file_path(__file__)
        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 36)

        self.__render = self.__font.render(self.__text, True, (255, 255, 255))
        self.__rect = self.__render.get_rect()
        
        self.__width = self.__rect.width
        self.__height = self.__rect.height

        super().__init__(state)

    def draw_at(self, surface: pygame.Surface, x: int, y: int) -> bool:
        self.__rect.topleft = (x, y)
        action = False
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.__render = self.__font.render(self.__text, True, (utils.pink))
                # depois opinem sobre esse ""
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
            self.clicked = False
            action = True
            self.__render = self.__font.render(self.__text, True, (255, 255, 255))
        surface.blit(self.__render, self.__rect.topleft)
        return action

    @property
    def width(self):
        return self.__width
    
    @property  
    def height(self):
        return self.__height