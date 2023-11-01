import pygame

class Mouse:
    def __init__(self) -> None:
        self.__image = pygame.transform.scale(pygame.image.load('../resources/cursor.webp'), (20, 20))
        self.__cursor_rect = self.__image.get_rect()
        pygame.mouse.set_visible(False)
        
    def show_mouse(self, screen):
        self.__cursor_rect.center = pygame.mouse.get_pos()
        screen.blit(self.__image, self.__cursor_rect)