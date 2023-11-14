import pygame
import math
from time import sleep

from utils.utils import get_file_path


class Bullet(pygame.sprite.Sprite):
    def __init__(
            self,
            direction,
            speed,
            x,
            y,
            range
        ) -> None:
        self.__speed = speed
        self.__position = [x, y]
        self.__direction = direction
        self.__color = 'red'
        self.__moving = True
        self.__range = range
        
        img = f'{get_file_path(__file__)}/bullet/fireball.webp'
        img_transform = pygame.transform.scale(pygame.image.load(img),
                                              (15, 15)) #image
        self.__image = pygame.transform.flip(img_transform, True, False)
        self.__image = pygame.transform.rotate(self.__image, 45)

    @property
    def moving(self):
        return self.__moving
 
    @moving.setter
    def moving(self, val:bool):
        if isinstance(val, bool):
            self.__moving = val

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val:list):
        if isinstance(val, list):
            self.__position = val

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, val:int):
        if isinstance(val, int):
            self.__direction = val

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val:int):
        if isinstance(val, int):
            self.__speed = val

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, val:int):
        if isinstance(val, int):
            self.__range = val

    def draw_at(self, screen:pygame.Surface) -> None:
        pygame.Surface.blit(screen, self.__image, self.__position)
        # pygame.draw.circle(screen, self.__color, self.__position, 5)

    def move(self) -> None:
        # calculos para que se mova na direção do mouse
        self.__position[0] += math.cos(self.__direction) * self.__speed
        self.__position[1] += math.sin(self.__direction) * self.__speed
        self.__range -= 1 * self.__speed
        if self.__range <= 0:
            self.__moving = False
        