from __future__ import annotations

import pygame

from abc import abstractmethod, ABC

class Character(ABC, pygame.sprite.Sprite):
    def __init__(
        self,
        position: pygame.Vector2,
        health: int,
        speed: int,
        sprite: pygame.surface.Surface,
        damage=5,
        armor=0,
        weapon=None,
        ) -> None:
        self.__position = position
        self.__health = health
        self.__damage = damage
        self.__speed_init = speed
        self.__speed = speed
        self.__armor = armor
        self.__weapon = weapon
        self.__sprite = sprite

        pygame.sprite.Sprite.__init__(self)

    @property
    def speed_init(self) -> int:
        return self.__speed_init

    @speed_init.setter
    def speed_init(self, speed_init: int) -> None:
        self.__speed_init = speed_init
        
    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        self.__health = health

    @abstractmethod
    def take_damage(self, damage: int) -> None:
        pass

    @abstractmethod
    def draw_at(self, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, self.__rect)

    @property
    def position(self) -> pygame.Vector2:
        return self.__position

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, val:int):
        if isinstance(val, int):
            self.__coordinate_y = val

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

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, val):
        self.__weapon = val

    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def attack(self) -> None:
        pass
