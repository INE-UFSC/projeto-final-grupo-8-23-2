from __future__ import annotations

import pygame

from weapons.weapon import Weapon
from weapons.earthquake import Earthquake
from constants import weapons_constants, img_names_constants
from utils.images.ImageGame import ImageGame


class Earthquaker(Weapon):
    def __init__(self, name, damage, range, sprite):
        super().__init__(name, damage, range, weapons_constants.EARTHQUAKER_RECOVER_TIME, sprite)
        self.__earthquake = None

    def attack(self, player_ref):
        if pygame.mouse.get_pressed()[0] and self.verify_attack_time():
            player_ref.attacking = True
        if player_ref.attacking and not pygame.mouse.get_pressed()[0]:
                self.shake(player_ref)
                self.attacking = True
                player_ref.attacking = False

    def check_target(self, seekers):
        for seeker in seekers:
            if self.__earthquake != None:
                verify_x = (seeker.position.x - self.__earthquake.position.x)**2 <= (self.__earthquake.range)**2
                verify_y = (seeker.position.y - self.__earthquake.position.y)**2 <= (self.__earthquake.range)**2
                if verify_x and verify_y:
                    seeker.take_damage(super().damage)
        self.__earthquake = None

    def shake(self, player_ref):
        self.__earthquake = Earthquake(player_ref.position.x, player_ref.position.y, super().range)


    def draw(self, screen:pygame.Surface):
        if self.attacking:
            position = (self.__earthquake.position.x - self.__earthquake.range, self.__earthquake.position.y - self.__earthquake.range)
            image = ImageGame().transform_flip(img_names_constants.EARTHQUAKE)
            pygame.Surface.blit(screen, image, position)
            self.attacking = False
