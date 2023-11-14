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
        self.__alive = True
        self.__radius = 20
        self.__seeker_position = pygame.Vector2(random.randint(seeker_constants.SPAWN_MARGIN, game_constants.SCREEN_WIDTH - seeker_constants.SPAWN_MARGIN), 
                                                random.randint(seeker_constants.SPAWN_MARGIN, game_constants.SCREEN_HEIGHT - seeker_constants.SPAWN_MARGIN))
        super().__init__(self.__seeker_position, seeker_constants.FIGHT_SEEKER_HEALTH, seeker_constants.FIGHT_SEEKER_SPEED, seeker_constants.FIGHT_SEEKER_DAMAGE, 
                         seeker_constants.FIGHT_SEEKER_ARMOR)

    def attack(self) -> None:
        self.__player_to_chase.take_damage(self.__damage)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'purple', self.__seeker_position, self.__seeker_range / 2)

    def take_damage(self, damage: int):
        if self.health <= 0:
            self.__alive = False

        self.health -= damage

    def collision_between_seeker_2(self, seeker_2, seeker_1_pos_x, seeker_1_pos_y):
        distance_between_seekers = math.sqrt((seeker_2.seeker_position.x - seeker_1_pos_x) ** 2 + (seeker_2.seeker_position.y - seeker_1_pos_y) ** 2)
        return distance_between_seekers <= self.__seeker_range
    
    def collision_between_seekers(self, seekers, seeker_1_pos_x, seeker_1_pos_y):
        for seeker in [x for x in seekers if x != self]:
            if self.collision_between_seeker_2(seeker, seeker_1_pos_x, seeker_1_pos_y):
                return True
        return False
        
    def move(self, seekers = None) -> None:
        # Cálculo da distância entre o seeker e o player para saber se o seeker
        # precisa continuar andando ou parar/atacar
        distance_between_seeker_and_player = math.sqrt((self.__player_to_chase.position.x - super().position.x) ** 2 + (self.__player_to_chase.position.y - super().position.y) ** 2)

        # Condicional que verifica se a distância entre o player e o seeker é maior que
        # o range do seeker em questão, caso seja, o seeker continua andando, caso contrário
        # o seeker não irá se movimentar
        if distance_between_seeker_and_player > self.__seeker_range:
            seeker_next_position_aux_y = self.__seeker_position.y + ((self.__player_to_chase.player_position.y - self.__seeker_position.y) / distance_between_seeker_and_player) * seeker_constants.FIGHT_SEEKER_SPEED
            seeker_next_position_aux_x = self.__seeker_position.x + ((self.__player_to_chase.player_position.x - self.__seeker_position.x) / distance_between_seeker_and_player) * seeker_constants.FIGHT_SEEKER_SPEED
            
            collision = False
            if seekers != None:
                collision = self.collision_between_seekers(seekers, seeker_next_position_aux_x, seeker_next_position_aux_y)
            if not collision:
                self.__seeker_position.y = seeker_next_position_aux_y
                self.__seeker_position.x = seeker_next_position_aux_x                
        else:
            self.attack()
            
    # Getters and Setters

    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, val:int):
        if isinstance(val, int):
            self.__damage = val

    @property
    def seeker_range(self):
        return self.__seeker_range
    
    @seeker_range.setter
    def seeker_range(self, val:int):
        if isinstance(val, int):
            self.__seeker_range = val

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, val:int):
        if isinstance(val, int):
            self.__radius = val

    @property
    def alive(self):
        return self.__alive
    
    @alive.setter
    def alive(self, val:bool):
        if isinstance(val, bool):
            self.__alive = val
        
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