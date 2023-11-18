import pygame
import math
from time import sleep

from utils.utils import get_file_path
from weapons.ammo import Ammo


class Bullet(Ammo):
    def __init__(self, x, y, range, speed, direction) -> None:
        super().__init__(x, y, range)
        self.__speed = speed
        self.__direction = direction
        self.__moving = True
        self.__range = range

        img = f'{get_file_path(__file__)}/bullet/fireball.webp'
        img_transform = pygame.transform.scale(pygame.image.load(img),
                                              (15, 15)) #image
        self.__image = pygame.transform.flip(img_transform, True, False)
        self.__image = pygame.transform.rotate(self.__image, 45)
        self.__rect = self.__image.get_rect()

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def moving(self):
        return self.__moving

    @moving.setter
    def moving(self, val:bool):
        if isinstance(val, bool):
            self.__moving = val

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

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.Surface.blit(screen, self.__image, super().position)
        pygame.draw.rect(self.__image, 'red', self.__rect)
        # pygame.draw.circle(screen, self.__color, self.__position, 5)

    def move(self) -> None:
        # calculos para que se mova na direção do mouse
        super().position[0] += math.cos(self.__direction) * self.__speed
        super().position[1] += math.sin(self.__direction) * self.__speed
        self.__range -= 1 * self.__speed
        if self.__range <= 0:
            self.__moving = False

