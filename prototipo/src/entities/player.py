from __future__ import annotations

import pygame
from entities import weapon, character
from constants import game_constants, player_constants, powerup_constants
from utils import health_bar
import math


class Player(character.Character):
    def __init__(self, experience: int=0, level: int=0, power_ups: list=[], score: int=0):
        self.__alive = True
        self.__player_position = pygame.Vector2(game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2)
        self.__weapon = weapon.Weapon('Pistol', 10, 400, 'pistol.png')
        self.__experience = experience
        self.__level = level
        self.__power_ups = power_ups
        self.__score = score
        self.__health = player_constants.HEALTH
        self.__health_bar = health_bar.HealthBar(self.__player_position, self.__health)
        self.__speed = player_constants.SPEED
        self.__attacking = False
        super().__init__(self.__player_position, self.__health, self.__speed)

    def attack(self, screen) -> None:
        if pygame.mouse.get_pressed()[0]:
            self.__attacking = True
        if self.__attacking and not pygame.mouse.get_pressed()[0]:
            dy = pygame.mouse.get_pos()[1] - self.__player_position.y
            dx = pygame.mouse.get_pos()[0] - self.__player_position.x
            angle = math.atan2(dy, dx)
            self.__weapon.shoot(angle, self.__player_position.x, self.__player_position.y)
            self.__attacking = False
        self.__weapon.draw(screen)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'blue', self.__player_position, player_constants.WIDTH)
        self.__health_bar.draw_at(screen)

    def take_damage(self, damage: int) -> None:
        if self.__health <= 0:
            self.__alive = False

        self.__health -= damage
        self.__health_bar.update_health_bar(self.__health)

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.__player_position.y > player_constants.WIDTH:
                self.__player_position.y -= self.__speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.__player_position.y < game_constants.SCREEN_HEIGHT - player_constants.WIDTH:
                self.__player_position.y += self.__speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.__player_position.x > player_constants.WIDTH:
                self.__player_position.x -= self.__speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.__player_position.x < game_constants.SCREEN_WIDTH - player_constants.WIDTH:
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

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, val):
        self.__health = val

    @property
    def health_bar(self):
        return self.__health_bar
    
    @health_bar.setter
    def health_bar(self, val):
        self.__health_bar = val

    def get_power_up(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            for powerup in self.__power_ups:
                # calculo da distancia entre o powerup e o player
                powerup_x = powerup.position.x
                powerup_y = powerup.position.y
                player_x = self.__player_position.x
                player_y = self.__player_position.y
                radius_player = player_constants.WIDTH
                radius_powerup = powerup_constants.width
                distance_formula = (math.sqrt(((powerup_x - player_x)**2) + ((powerup_y - player_y)**2)))
                # condição para usar o powerup
                if (not powerup.actived) and (distance_formula <= (radius_player + radius_powerup)) :
                    powerup.activate_power_up()
