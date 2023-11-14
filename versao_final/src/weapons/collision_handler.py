import pygame


class CollisionHandler:
    def __init__(self, entities_list: list, entities_list2: list, dokill: bool, dokill2: bool) -> None:
        self.__entities_list1 = entities_list
        self.__entities_list2 = entities_list2
        self.__dokill = dokill
        self.__dokill2 = dokill2

    def detect_collision(self) -> dict:
        collisions = pygame.sprite.groupcollide(
        self.__entities_list1,
        self.__entities_list2,
        self.__dokill,
        self.__dokill2
        )
        return collisions