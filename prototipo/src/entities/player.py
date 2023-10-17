from __future__ import annotations

import pygame
from entities import weapon, character
from constants import game_constants, player_constants


class Player(character.Character):
    def __init__(self, weapon=None, experience: int=0, level: int=0, power_ups: list=[], score: int=0):
        self.__alive = True
        self.__player_position = pygame.Vector2(game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2)
        self.__weapon = weapon
        self.__experience = experience
        self.__level = level
        self.__power_ups = power_ups
        self.__score = score
        self.__health = player_constants.HEALTH
        self.__speed = player_constants.SPEED
        super().__init__(self.__player_position, self.__health, self.__speed)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'blue', self.__player_position, 40)

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.__player_position.y -= self.__speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.__player_position.y += self.__speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.__player_position.x -= self.__speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.__player_position.x += self.__speed

    @property
    def player_position(self) -> pygame.Vector2:
        return self.__player_position

    @player_position.setter
    def player_position(self, player_position: pygame.Vector2) -> None:
        self.__player_position = player_position

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, val: weapon.Weapon):
        if isinstance(val, weapon.Weapon):
            self.__weapon = val

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, val:int):
        if isinstance(val, int):
            self.__experience = val

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, val:int):
        if isinstance(val, int):
            self.__level = val

    @property
    def power_ups(self):
        return self.__power_ups

    @power_ups.setter
    def power_ups(self, val:list):
        if isinstance(val, list):
            self.__power_ups = val

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val:int):
        if isinstance(val, int):
            self.__score = val
