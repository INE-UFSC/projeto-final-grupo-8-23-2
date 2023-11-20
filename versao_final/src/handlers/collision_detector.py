import pygame


class CollisionDetector:
    def __init__(self, entities_list: list[pygame.sprite.Sprite], entities_list2: list[pygame.sprite.Sprite]) -> None:
        self._entities_list = entities_list
        self._entities_list2 = entities_list2

    def detect_collision(self) -> dict:
        entities_list_group = pygame.sprite.Group()
        entities_list_group.add(self._entities_list)

        entities_list2_group = pygame.sprite.Group()
        entities_list2_group.add(self._entities_list2)

        collisions = pygame.sprite.groupcollide(entities_list_group, entities_list2_group, False, False)
        return collisions

