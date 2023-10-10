import pygame

class Button:
    def __init__(self, height: int, width: int, coordinate_x: int, coordinate_y: int, icon: str):
       self.__height = height
       self.__width = width
       self.__coordinate_x = coordinate_x
       self.__coordinate_y = coordinate_y
       self.__icon = icon
       self.__clicked = False
       self.__rect = self.__icon.get_rect()

    def click_button(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.__clicked == False:
                action = True
                self.__clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.__clicked = False
        surface.blit(self.__icon, (self.__rect.x, self.__rect.y))
        return action

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val:int):
        if isinstance(val, int):
            self.__height = val

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val:int):
        if isinstance(val, int):
            self.__width = val

    @property
    def coordinate_x(self):
        return self.__coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, val:int):
        if isinstance(val, int):
            self.__coordinate_x = val

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, val:int):
        if isinstance(val, int):
            self.__coordinate_y = val

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, val:str):
        if isinstance(val, str):
            self.__icon = val
