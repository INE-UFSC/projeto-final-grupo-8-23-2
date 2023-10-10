from __future__ import annotations

import pygame

from abc import abstractmethod, ABC
from constants import game_constants

class Character(ABC):
    def __init__(self, character_position: pygame.Vector2, health: int, damage: int, speed: int, sprite: str, armor: float):
        self.__character_position = character_position
        self.__health = health
        self.__damage = damage
        self.__speed = speed
        self.__armor = armor
        self.__sprite = sprite
        self.__rect = None

    @abstractmethod
    def draw_at(self, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, self.__rect)

    @property
    def character_position(self) -> pygame.Vector2:
        return self.__character_position

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, val:int):
        if isinstance(val, int):
            self.__coordinate_y = val

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, val:int):
        if isinstance(val, int):
            self.__health = val

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, val:int):
        if isinstance(val, int):
            self.__damage = val

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val:int):
        if isinstance(val, int):
            self.__speed = val

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, val:str):
        if isinstance(val, str):
            self.__sprite = val

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, val:float):
        if isinstance(val, float):
            self.__armor = val

    @abstractmethod
    def move() -> None:
        pass

    # @abstractmethod
    # def attack() -> None:
    #     pass
