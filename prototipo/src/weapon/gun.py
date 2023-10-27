from weapon.bullet import Bullet
from abc import ABC, abstractmethod

from weapon.weapon import Weapon


class Gun(Weapon):
    def __init__(self, name: str, range: int, damage: int, sprite: str, bullets: list[Bullet]) -> None:
        super().__init__(name, range, damage, sprite)
        self.__name = name
        self.__range = range
        self.__damage = damage
        self.__sprite = sprite
        self.__bullets = bullets

    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets

    @bullets.setter
    def bullets(self, val: list[Bullet]):
        if isinstance(val, list):
            self.__bullets = val

    def attack(self, angle, player_x, player_y) -> None:
        bullet = Bullet(angle, 10, player_x, player_y, self.__range)
        self.__bullets.append(bullet)

    def draw(self, screen) -> None:
        for bullet in self.__bullets:
            bullet.draw_at(screen)
            bullet.move()
            if not bullet.moving:
                self.__bullets.remove(bullet)
