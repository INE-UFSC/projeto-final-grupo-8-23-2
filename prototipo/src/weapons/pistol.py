from abc import ABC, abstractmethod
import pygame
import math

from weapons.weapon import Weapon
from weapons.bullet import Bullet


class Pistol(Weapon):
    def __init__(self, name: str, damage: int, range: int, sprite: str) -> None:
        super().__init__(name, damage, range, sprite)
        self.__bullets = []

    def attack(self, screen, angle, player_x, player_y) -> None:
        bullet = Bullet(angle, 10, player_x, player_y, self.__range)
        self.__bullets.append(bullet)
        if pygame.mouse.get_pressed()[0]:
            self.__attacking = True
        if self.__attacking and not pygame.mouse.get_pressed()[0]:
            dy = pygame.mouse.get_pos()[1] - super().position.y
            dx = pygame.mouse.get_pos()[0] - super().position.x
            angle = math.atan2(dy, dx)
            self.__weapon.shoot(angle, super().position.x, super().position.y)
            self.__attacking = False
        self.__weapon.draw(screen)

    def draw(self, screen: pygame.Surface) -> None:
        for bullet in self.__bullets:
            bullet.draw_at(screen)
            bullet.move()
            if not bullet.moving:
                self.__bullets.remove(bullet)

    @property
    def bullets(self) -> list:
        return self.__bullets
