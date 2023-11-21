from __future__ import annotations

import pygame
import math

from entities import character
from utils.images.ImageGame import ImageGame
from constants import img_names_constants
from utils.music import Music
from weapons import weapon
from weapons.gun import Gun
from weapons.earthquaker import Earthquaker
from constants import game_constants, player_constants, powerup_constants, direction_constants, names_musics
from utils import health_bar
from utils.utils import get_file_path

class Player(character.Character):
    def __init__(
        self,
        weapon: weapon.Weapon,
        experience: int=0,
        level: int=0,
        power_ups: list=[],
        score: int=0
        ) -> None:
        self.__alive = True
        self.__weapon = weapon
        self.__experience = experience
        self.__level = level
        self.__power_ups = power_ups
        self.__score = score
        self.__death_player_draw = False
        self.__current_direction = None
        self.__spawn_position = pygame.Vector2(player_constants.PLAYER_SPAWN_POSITION)
        self.__health_bar = health_bar.HealthBar(self.__spawn_position, player_constants.HEALTH)
        self.__attacking = False
        # era flip
        self.image = ImageGame().transform_scale(img_names_constants.PLAYER)

        super().__init__(self.__spawn_position, player_constants.HEALTH, player_constants.SPEED, self.image)

    def attack(self, screen: pygame.Surface) -> None:
        self.__weapon.attack(self)

    def draw_at(self, screen: pygame.Surface, position = None) -> None:
        if self.alive:
            self.set_img_by_direction()
        pos = super().position if position == None else position
        pygame.Surface.blit(screen, self.image, pos)
        self.__health_bar.draw_at(screen)
        self.__weapon.draw(screen, self)

    def set_img_by_direction(self):
        match self.__current_direction:
            case direction_constants.LEFT:
                self.set_img_draw_left()
            case direction_constants.RIGHT:
                self.set_img_draw_right()
            case _:
                return

    def set_img_draw_right(self):
        self.image = ImageGame().transform_scale(img_names_constants.RUN_PLAYER)

    def set_img_draw_left(self):
        self.image = ImageGame().transform_flip(img_names_constants.RUN_PLAYER, True)

    def draw_at_death(self, screen: pygame.Surface):
        is_left = self.__current_direction == 'LEFT'
        self.image = ImageGame().transform_flip(img_names_constants.DEATH_PLAYER, is_left)
        position = pygame.Vector2(super().position.x, super().position.y + 35)

        self.draw_at(screen, position=position)
        self.__death_player_draw = True

    def take_damage(self, damage: int) -> None:
        if self.health <= 0:
            self.__alive = False

        if self.__alive:
            self.health -= damage
        self.__health_bar.update_health_bar(self.health)

    def move(self):
        if self.alive:
            keys = pygame.key.get_pressed()
            direction = None
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                direction = 'UP'
                if super().position.y > player_constants.WIDTH:
                    super().position.y -= super().speed
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                direction = 'DOWN'
                if super().position.y < game_constants.SCREEN_HEIGHT - player_constants.WIDTH:
                    super().position.y += super().speed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                direction = 'LEFT'
                if super().position.x > player_constants.WIDTH:
                    super().position.x -= super().speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                direction = 'RIGHT'
                if super().position.x < game_constants.SCREEN_WIDTH - player_constants.WIDTH:
                    super().position.x += super().speed

            if direction != None:
                self.__current_direction = direction
            
    def add_score(self, worth_points):
        self.score += worth_points

    def get_power_up(self, screen):
        for powerup in self.__power_ups:
            # calculo da distancia entre o powerup e o player
            powerup_x = powerup.position.x
            powerup_y = powerup.position.y
            player_x = self.position.x
            player_y = self.position.y
            radius_player = player_constants.WIDTH
            radius_powerup = powerup_constants.WIDTH
            distance_formula = (math.sqrt(((powerup_x - player_x)**2) + ((powerup_y - player_y)**2)))
            # condição para usar o powerup
            if (not powerup.actived) and (distance_formula <= (radius_player + radius_powerup)) :
                powerup.activate_power_up(screen)
                Music().run_sound(names_musics.COIN)
            
    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, val:bool):
        if isinstance(val, bool):
            self.__alive = val

    @property
    def player_position(self):
        return self.__player_position

    @player_position.setter
    def player_position(self, val:pygame.Vector2):
        if isinstance(val, pygame.Vector2):
            self.__player_position = val

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, val):
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
    def health_bar(self):
        return self.__health_bar

    @health_bar.setter
    def health_bar(self, val:health_bar.HealthBar):
        if isinstance(val, health_bar.HealthBar):
            self.__health_bar = val

    @property
    def attacking(self):
        return self.__attacking

    @attacking.setter
    def attacking(self, val:bool):
        if isinstance(val, bool):
            self.__attacking = val

    @property
    def current_direction(self):
        return self.__current_direction

    @current_direction.setter
    def direction(self, val):
        if isinstance(val, str):
            self.__current_direction = val

    @property
    def death_player_draw(self):
        return self.__death_player_draw

