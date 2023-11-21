from __future__ import annotations

import pygame
import math

from constants import weapons_constants
from entities import player
from weapons.weapon import Weapon
from weapons.bullet import Bullet
import game


class Gun(Weapon):
    def __init__(self, name, damage, range, sprite, game_ref: game.Game):
        super().__init__(name, damage, range, weapons_constants.GUN_RECOVER_TIME, sprite, game_ref)
        self.__bullets = []
        self.__attacking = False

    @property
    def bullets(self):
        return self.__bullets

    @bullets.setter
    def bullets(self, bullets):
        if isinstance(bullets, list):
            self.__bullets = bullets

    def attack(self, player_ref: player.Player):
        if pygame.mouse.get_pressed()[0]:
            self.__attacking = True
        if self.__attacking and not pygame.mouse.get_pressed()[0]:
            dy = pygame.mouse.get_pos()[1] - player_ref.position.y
            dx = pygame.mouse.get_pos()[0] - player_ref.position.x
            angle = math.atan2(dy, dx)
            self.shoot(angle, player_ref.position.x, player_ref.position.y)
            self.__attacking = False

    def draw(self, screen: pygame.Surface):
        for bullet in self.__bullets:
            bullet.draw_at(screen)
            bullet.move()
            if not bullet.moving:
                self.__bullets.remove(bullet)

    def shoot(self, angle, player_x, player_y) -> None:
        bullet = Bullet(player_x + 45, player_y + 30, super().range, 10, angle)
        self.__bullets.append(bullet)