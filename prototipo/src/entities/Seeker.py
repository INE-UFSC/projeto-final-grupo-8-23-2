from abc import abstractmethod, ABC
import pygame
import random

from Player import Player
from Character import Character
from constants import game_constants


class Seeker(Character, ABC):
    def __init__(self):
       self.__player_to_chase = None
       super().__init__(pygame.Vector2(game_constants.screen_width / 2 + 300, game_constants.screen_height / 2 + 300), 300, 20, 50, pygame.draw.circle(game_constants.screen, 'red', (game_constants.screen_width / 2 + 400, game_constants.screen_height / 2 + 400), 20), 30.0)

    @property
    def player_to_chase(self):
        return self.__player_to_chase

    @player_to_chase.setter
    def player_to_chase(self, val:Player):
        if isinstance(val, Player):
            self.__player_to_chase = val

    @abstractmethod
    def chase_player(self) -> None:
        pass

    @abstractmethod
    def special_ability(self) -> None:
        pass
