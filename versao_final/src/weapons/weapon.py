from __future__ import annotations

import pygame
from abc import ABC, abstractmethod

import game


class Weapon(ABC):
    def __init__(self, name, damage, range, recover_time: int, sprite, game_ref: game.Game):
        self.__name = name
        self.__damage = damage
        self.__range = range
        self.__sprite = sprite
        self.__bullets = []

        self.__game_ref = game_ref
        self.__last_attack = 0
        self.__recover_time = recover_time

        self.__attacking = False

    def verify_attack_time(self) -> bool:
        if pygame.time.get_ticks() - self.last_attack < self.recover_time:
            return False
        self.last_attack = pygame.time.get_ticks()
        return True

    @property
    def recover_time(self) -> int:
        return self.__recover_time

    @recover_time.setter
    def recover_time(self, recover_time: int) -> None:
        self.__recover_time = recover_time

    @property
    def last_attack(self) -> int:
        return self.__last_attack

    @last_attack.setter
    def last_attack(self, last_attack_time: int) -> None:
        self.__last_attack = last_attack_time

    @property
    def game_ref(self) -> game.Game:
        return self.__game_ref

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def draw(self):
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
    
    #crie getters e setters para os atributos restantes

    @property
    def attacking(self) -> bool:
        return self.__attacking
    
    @attacking.setter
    def attacking(self, val: bool) -> None:
        if isinstance(val, bool):
            self.__attacking = val
