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
        bullets_to_remove = []

        for bullet, seekers in collisions.items():
            bullets_to_remove.append(bullet)
            for seeker in seekers:
                seeker.take_damage(self.__weapon.damage)

        for bullet in bullets_to_remove:
            self.__bullets_list.remove(bullet)

