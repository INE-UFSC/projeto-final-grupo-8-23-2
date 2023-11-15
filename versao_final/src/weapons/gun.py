from weapons.weapon import Weapon
from weapons.bullet import Bullet

import pygame
import math



class Gun(Weapon):
    def __init__(self, name, damage, range, sprite):
        super().__init__(name, damage, range, sprite)
        self.__bullets = []

    @property
    def bullets(self):
        return self.__bullets
    
    @bullets.setter
    def bullets(self, bullets):
        if isinstance(bullets, list):
            self.__bullets = bullets

    def attack(self, player_ref):
        if pygame.mouse.get_pressed()[0]:
            player_ref.attacking = True
        if player_ref.attacking and not pygame.mouse.get_pressed()[0]:
            dy = pygame.mouse.get_pos()[1] - player_ref.position.y
            dx = pygame.mouse.get_pos()[0] - player_ref.position.x
            angle = math.atan2(dy, dx)
            self.shoot(angle, player_ref.position.x, player_ref.position.y)
            player_ref.attacking = False
    
    def draw(self, screen: pygame.Surface):
        for bullet in self.__bullets:
            bullet.draw_at(screen)
            bullet.move()
            if not bullet.moving:
                self.__bullets.remove(bullet)

    def check_target(self, seeker):
        for bullet in self.__bullets:
            if seeker.position[0] - seeker.radius <= bullet.position[0] <= seeker.position[0] + seeker.radius and \
                    seeker.position[1] - seeker.radius <= bullet.position[1] <= seeker.position[1] + seeker.radius:
                seeker.take_damage(super().damage)
                bullet.moving = False

    def shoot(self, angle, player_x, player_y) -> None:
        bullet = Bullet(angle, 10, player_x + 45, player_y + 30, super().range)
        self.__bullets.append(bullet)
