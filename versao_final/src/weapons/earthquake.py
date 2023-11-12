import pygame
from abc import ABC, abstractmethod

from weapons.weapon import Weapon
from weapons.bullet import Bullet


class Earthquaker(Weapon):
    def __init__(self, name, damage, range, sprite):
        super().__init__(name, damage, range, sprite)
        self.__earthquakes = []

    def attack(self, player_position):
        pass

    def draw(self):
        pass