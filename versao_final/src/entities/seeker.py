from abc import ABC
import pygame
import random
import math

from entities.player import Player
from entities.character import Character
from constants import game_constants
from constants import seeker_constants
from utils.images.ImageGame import ImageGame
from constants import img_names_constants

class Seeker(Character, ABC):
    def __init__(self, player_reference: Player, seeker_range: int, seeker_health: int,
                 seeker_speed: int, seeker_damage: int, seeker_armor: int, worth_points:int) -> None:
        self.image = ImageGame().transform_scale(img_names_constants.GHOST)
        self.__player_to_chase = player_reference
        self.__seeker_range = seeker_range
        self.__damage = seeker_damage
        self.__alive = True
        self.__radius = 20
        self.__seeker_position = self.define_spawn_position()
        self.__inverted = False
        self.__alpha_draw = 100
        self.__worth_points = worth_points

        super().__init__(self.__seeker_position, seeker_health, seeker_speed, self.image, seeker_armor)
        if super().position.x <= self.__player_to_chase.position.x:
            self.image = ImageGame().transform_flip(img_names_constants.GHOST, True)
            self.__inverted = True

        self.rect = self.image.get_rect()
        self.rect.topleft = (int(self.position.x), int(self.position.y))

    def attack(self) -> None:
        self.__player_to_chase.take_damage(self.__damage)

    def define_spawn_position(self) -> pygame.Vector2:
        vertical_or_horizontal = random.choice(['vertical', 'horizontal'])
        if vertical_or_horizontal == 'horizontal':
            x = random.choice([0, game_constants.SCREEN_WIDTH])
            y = random.choice(list(range(0, game_constants.SCREEN_HEIGHT, self.__radius * 2)))
        elif vertical_or_horizontal == 'vertical':
            x = random.choice(list(range(0, game_constants.SCREEN_WIDTH, self.__radius * 2)))
            y = random.choice([0, game_constants.SCREEN_HEIGHT])
        return pygame.Vector2(x, y)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.Surface.blit(screen, self.image, self.__seeker_position)

    def take_damage(self, damage: int):
        if int(self.health) <= int(0):
            self.__alive = False
        self.health -= damage
        self.__alpha_draw -= 10
        self.image.set_alpha(self.__alpha_draw)
        pass

    def move(self) -> None:
        self.invert()
        distance_between_seeker_and_player = math.sqrt((self.__player_to_chase.position.x - super().position.x) ** 2 + (self.__player_to_chase.position.y - super().position.y) ** 2)
        if distance_between_seeker_and_player > self.__seeker_range:
            super().position.y += ((self.__player_to_chase.position.y - super().position.y) / distance_between_seeker_and_player) * seeker_constants.FIGHT_SEEKER_SPEED
            super().position.x += ((self.__player_to_chase.position.x - super().position.x) / distance_between_seeker_and_player) * seeker_constants.FIGHT_SEEKER_SPEED
        else:
            self.attack()
        self.rect.topleft = (int(self.position.x), int(self.position.y))

    def invert(self):
        if self.__inverted == False and super().position.x <= self.__player_to_chase.position.x:
            self.image = pygame.transform.flip(self.image, True, False)
            self.__inverted = True
        elif self.__inverted == True and super().position.x > self.__player_to_chase.position.x:
            self.image = pygame.transform.flip(self.image, True, False)
            self.__inverted = False

    def give_points(self):
        self.__player_to_chase.score += self.__worth_points

    @property
    def worth_points(self):
        return self.__worth_points

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
