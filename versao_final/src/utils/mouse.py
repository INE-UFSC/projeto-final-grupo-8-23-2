import pygame

from utils.utils import get_file_path


class Mouse:
    def __init__(self) -> None:
        resources_path = get_file_path(__file__)

        self.__image = pygame.transform.scale(pygame.image.load(f'{resources_path}/cursors/cursor.webp'), (20, 20))
        self.__cursor_rect = self.__image.get_rect()

        pygame.mouse.set_visible(False)

    def show_mouse(self, screen: pygame.Surface) -> None:
        self.__cursor_rect.center = pygame.mouse.get_pos()
        screen.blit(self.__image, self.__cursor_rect)
