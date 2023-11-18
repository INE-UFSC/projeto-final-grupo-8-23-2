import pygame

from weapons import weapon
from entities import seeker


class BulletCollisionHandler:
    def __init__(self, weapon_ref: weapon.Weapon, seekers_list_ref: list[seeker.Seeker]) -> None:
        if hasattr(weapon_ref, 'bullets'):
            self.__bullets_list = weapon_ref.bullets
        else:
            return
        self.__weapon = weapon_ref
        self.__seekers_list = seekers_list_ref

    def handle_collision(self, collisions: dict) -> None:
        for bullet, seeker in collisions.items():
            self.__bullets_list.remove(bullet)
            seeker.take_damage(self.__weapon.damage)
            if seeker.health <= 0:
                self.__seekers_list.remove(seeker)

