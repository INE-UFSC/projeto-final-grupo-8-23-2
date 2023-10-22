from abc import ABC
import pygame
import random
import math

from entities.player import Player
from entities.character import Character
from constants import game_constants
from constants import seeker_constants


class Seeker(Character, ABC):
    def __init__(
        self,
        player_reference: Player,
        seeker_range: int,
        seeker_damage: int
        ) -> None:
        self.__player_to_chase = player_reference
        self.__seeker_range = seeker_range
        self.__damage = seeker_damage
        super().__init__(pygame.Vector2(random.randint(seeker_constants.SPAWN_MARGIN, game_constants.SCREEN_WIDTH - seeker_constants.SPAWN_MARGIN), random.randint(seeker_constants.SPAWN_MARGIN, game_constants.SCREEN_HEIGHT - seeker_constants.SPAWN_MARGIN)), seeker_constants.FIGHT_SEEKER_HEALTH, seeker_constants.FIGHT_SEEKER_SPEED, seeker_constants.FIGHT_SEEKER_DAMAGE, seeker_constants.FIGHT_SEEKER_ARMOR)

    def attack(self) -> None:
        self.__player_to_chase.take_damage(self.__damage)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'purple', super().position, 20)

    @property
    def position(self):
        return super().position

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
        distance_between_seeker_and_player = math.sqrt((self.__player_to_chase.position.x - super().position.x) ** 2 + (self.__player_to_chase.position.y - super().position.y) ** 2)

        # Condicional que verifica se a distância entre o player e o seeker é maior que
        # o range do seeker em questão, caso seja, o seeker continua andando, caso contrário
        # o seeker não irá se movimentar
        if distance_between_seeker_and_player > self.__seeker_range:
            super().position.y += ((self.__player_to_chase.position.y - super().position.y) / distance_between_seeker_and_player) * seeker_constants.FIGHT_SEEKER_SPEED
            super().position.x += ((self.__player_to_chase.position.x - super().position.x) / distance_between_seeker_and_player) * seeker_constants.FIGHT_SEEKER_SPEED
        else:
            self.attack()
