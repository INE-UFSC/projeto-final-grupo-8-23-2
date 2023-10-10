from abc import abstractmethod, ABC
import pygame
import random

from Player import Player
from Character import Character
from constants import game_constants


class Seeker(Character, ABC):

    def __init__(self, player_reference: Player):
        self.__player_to_chase = player_reference
        super().__init__(pygame.Vector2(game_constants.screen_width / 2 + 300, game_constants.screen_height / 2 + 300), 300, 20, 50, pygame.draw.circle())

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
