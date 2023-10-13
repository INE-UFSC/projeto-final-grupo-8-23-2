from abc import abstractmethod, ABC
import pygame
import random
from entities.player import Player
from entities.character import Character
from constants import game_constants


class Seeker(Character, ABC):

    def __init__(self, player_reference=None):
        self.__player_to_chase = player_reference
        self.__seeker_position = pygame.Vector2(random.randint(0, game_constants.SCREEN_WIDTH), random.randint(0, game_constants.SCREEN_HEIGHT))
        super().__init__(self.__seeker_position, 300, 20, 50, 30.0)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'purple', self.__seeker_position, 20)

    @property
    def player_to_chase(self):
        return self.__player_to_chase

    @player_to_chase.setter
    def player_to_chase(self, val:Player):
        if isinstance(val, Player):
            self.__player_to_chase = val

    def move(self) -> None:
        vel = 10
        while self.player_to_chase.player_position != self.__seeker_position:
            self.__seeker_position.y += ((self.player_to_chase.player_position.y - self.__seeker_position.y)/abs(self.player_to_chase.player_position.y - self.__seeker_position.y)) * vel
            self.__seeker_position.x += ((self.player_to_chase.player_position.x - self.__seeker_position.x)/abs(self.player_to_chase.player_position.x - self.__seeker_position.x)) * vel
        
        # player_position = self.player_to_chase.player_position
        # seeker_position = self.__seeker_position
        # enquanto as coordenadas dos seekers e dos personagens forem diferentes
        # pega a velocidade e mutiplica por 1 ou -1 (para saber se precisa ir para frente ou tras / direita ou esquerda)
        # chego nesse resultado entre 1 ou -1 pela divisao entre a subtracao das distancias dividido pelo modulo da subtracao das distancias
        # por exemplo, seeker (30, 20) e personagem (30, 40) resultado da divisao vai dar 1

    # @abstractmethod
    # def special_ability(self) -> None:
    #     pass
