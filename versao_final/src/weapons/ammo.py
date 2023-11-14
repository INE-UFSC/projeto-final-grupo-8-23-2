from abc import ABC, abstractmethod
import pygame



class Ammo(ABC):
    def __init__(self, x, y, range) -> None:
        self.__position = pygame.Vector2(x, y)
        self.__range = range

    @property
    def position(self):
        return self.__position
    
    @property
    def range(self):
        return self.__range
    
    @abstractmethod
    def draw_at(self):
        pass
