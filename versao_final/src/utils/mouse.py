import pygame

from utils.utils import get_file_path

from utils.images.ImageGame import ImageGame
from constants import img_names_constants
class Mouse:
    def __init__(self) -> None:
        resources_path = get_file_path(__file__)

        self.__image = ImageGame().transform_scale(img_names_constants.CURSOR)
        self.__cursor_rect = self.__image.get_rect()

        pygame.mouse.set_visible(False)

    def show_mouse(self, screen: pygame.Surface) -> None:
        self.__cursor_rect.center = pygame.mouse.get_pos()
        screen.blit(self.__image, self.__cursor_rect)
