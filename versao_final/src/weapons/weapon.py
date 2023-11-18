import pygame
from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, name, damage, range, sprite):
        self.__name = name
        self.__damage = damage
        self.__range = range
        self.__sprite = sprite
        self.__bullets = []

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def check_target(self):
        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, val:str) -> None:
        if isinstance(val, str):
            self.__name = val

    @property
    def damage(self) -> int:
        return self.__damage

    @damage.setter
    def damage(self, val: int) -> None:
        if isinstance(val, int):
            self.__damage = val

    @property
    def range(self) -> int:
        return self.__range

    @range.setter
    def range(self, val:int) -> None:
        if isinstance(val, int):
            self.__range = val

    @property
    def sprite(self) -> str:
        return self.__sprite

    @sprite.setter
    def sprite(self, val: str) -> None:
        if isinstance(val, str):
            self.__sprite = val

    @property
    def bullets(self):
        return self.__bullets
