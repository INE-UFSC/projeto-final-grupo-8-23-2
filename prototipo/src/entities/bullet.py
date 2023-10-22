import pygame
import math
from constants import game_constants

class Bullet:
    def __init__(self, direction, speed) -> None:
        self.__rect = pygame.Rect(0, 0, 10, 10)
        self.__speed = speed
        self.__direction = direction
        self.__color = 'red'

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, val:pygame.Rect):
        if isinstance(val, pygame.Rect):
            self.__rect = val

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, val:int):
        if isinstance(val, int):
            self.__speed = val

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, val:pygame.Vector2):
        if isinstance(val, pygame.Vector2):
            self.__direction = val

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, val:str):
        if isinstance(val, str):
            self.__color = val

    def draw_at(self, screen:pygame.Surface) -> None:
        pygame.draw.rect(screen, self.__color, self.__rect)

    def move(self) -> None:
        # calculos para que se mova na direção do mouse
        self.__rect.x += math.cos(self.__direction) * self.__speed
        self.__rect.y += math.sin(self.__direction) * self.__speed