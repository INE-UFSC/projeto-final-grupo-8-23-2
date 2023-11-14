import pygame
from abc import ABC, abstractmethod

from weapons.weapon import Weapon

class Earthquaker(Weapon):
    def __init__(self, name, damage, range, sprite):
        super().__init__(name, damage, range, sprite)
        self.__earthquake = []

    def attack(self, player_ref):
        if pygame.mouse.get_pressed()[0]:
            player_ref.attacking = True
        if player_ref.attacking and not pygame.mouse.get_pressed()[0]:
            self.shake(player_ref)
            player_ref.attacking = False

    def check_target(self, seeker):
        if self.__earthquake != None:
            if ((seeker.position.x - self.__earthquake[0])**2) + ((seeker.position.y - self.__earthquake[1])**2) <= (self.__earthquake[2])**2:
                seeker.take_damage(super().damage)
        self.__earthquake = None

    def shake(self, player_ref):
        self.__earthquake = (player_ref.position.x, player_ref.position.y, super().range)

    def draw(self, screen):
        pass