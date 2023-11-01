import pygame

from utils.utils import get_file_path
from utils import utils


class Button:
    def __init__(self, text: str, state) -> None:
        self.__text = text
        self.__clicked = False

        # Encontra o caminho até a pasta resources
        resources_path = get_file_path(__file__)
        self.__font = pygame.font.Font(f'{resources_path}/fonts/NightsideDemoRegular.ttf', 36)

        self.__render = self.__font.render(self.__text, True, (255, 255, 255))
        self.__rect = self.__render.get_rect()
        self.__next_state = state

    def draw_at(self, surface: pygame.Surface, x: int, y: int) -> bool:
        self.__rect.topleft = (x, y)
        action = False
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.__clicked:
                self.__clicked = True
                self.__render = self.__font.render(self.__text, True, (utils.pink))
                # depois opinem sobre esse ""
        if pygame.mouse.get_pressed()[0] == 0 and self.__clicked:
            self.__clicked = False
            action = True
            self.__render = self.__font.render(self.__text, True, (255, 255, 255))
        surface.blit(self.__render, self.__rect.topleft)
        return action

    def get_clicked(self) -> bool:
        return self.__clicked

    @property
    def next_state(self):
        return self.__next_state

    @property
    def width(self):
        return self.__rect.width

