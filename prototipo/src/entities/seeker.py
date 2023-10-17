from abc import abstractmethod, ABC
import pygame
import random
import math

from entities.player import Player
from entities.character import Character
from constants import game_constants
from constants import seeker_constants


class Seeker(Character, ABC):

    def __init__(self, player_reference: Player, seeker_range: int) -> None:
        self.__player_to_chase = player_reference
        self.__seeker_position = pygame.Vector2(random.randint(0, game_constants.SCREEN_WIDTH), random.randint(0, game_constants.SCREEN_HEIGHT))
        self.__seeker_range = seeker_range
        super().__init__(self.__seeker_position, 300, 20, 50, 30.0)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'purple', self.__seeker_position, 20)

    @property
    def player_to_chase(self) -> Player:
        return self.__player_to_chase

    @player_to_chase.setter
    def player_to_chase(self, player_to_chase: Player) -> None:
        if isinstance(player_to_chase, Player):
            self.__player_to_chase = player_to_chase

    def move(self) -> None:
        # Cálculo da distância entre o seeker e o player para saber se o seeker
        # precisa continuar andando ou parar/atacar
        distance_between_seeker_and_player = math.sqrt((self.__player_to_chase.player_position.x - self.__seeker_position.x) ** 2 + (self.__player_to_chase.player_position.y - self.__seeker_position.y) ** 2)

        # Condicional que verifica se a distância entre o player e o seeker é maior que
        # o range do seeker em questão, caso seja, o seeker continua andando, caso contrário
        # o seeker não irá se movimentar
        if distance_between_seeker_and_player > self.__seeker_range:
            self.__seeker_position.y += ((self.__player_to_chase.player_position.y - self.__seeker_position.y) / distance_between_seeker_and_player) * seeker_constants.SEEKER_SPEED
            self.__seeker_position.x += ((self.__player_to_chase.player_position.x - self.__seeker_position.x) / distance_between_seeker_and_player) * seeker_constants.SEEKER_SPEED

    # @abstractmethod
    # def special_ability(self) -> None:
    #     pass
