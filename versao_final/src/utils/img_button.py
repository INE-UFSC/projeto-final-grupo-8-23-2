import pygame

from utils.button import Button


class ImgButton(Button):
    def __init__(self, img: str, state) -> None:
        self.__img = pygame.transform.scale(pygame.image.load(img), (50, 50))
        self.__rect = self.__img.get_rect()
        self.__width = self.__rect.width
        super().__init__(state)

    def draw_at(self, surface: pygame.Surface, x: int, y: int) -> bool:
        self.__rect.topleft = (x, y)
        action = False
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                # depois opinem sobre esse ""
        if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
            self.clicked = False
            action = True
        surface.blit(self.__img, self.__rect)
        return action
    
    # Getters and Setters
    
    @property
    def width(self):
        return self.__width