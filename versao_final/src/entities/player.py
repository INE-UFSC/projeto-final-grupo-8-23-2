from __future__ import annotations
import random
import pygame
import math


from entities import character
from weapons.gun import Gun
from weapons.earthquaker import Earthquaker
from constants import game_constants, player_constants, powerup_constants, direction_constants
from utils import health_bar
from utils.utils import get_file_path


class Player(character.Character):
    def __init__(
        self,
        experience: int=0,
        level: int=0,
        power_ups: list=[],
        score: int=0
        ) -> None:
        self.__alive = True
        # self.__weapon = Gun('Pistol', 10, 400, 'pistol.png')
        self.__weapon = Earthquaker("Earthquake", 10, 400, None)
        self.__experience = experience
        self.__level = level
        self.__power_ups = power_ups
        self.__score = score
        self.__death_player_draw = False
        self.__current_direction = None
        self.__spawn_position = pygame.Vector2(player_constants.PLAYER_SPAWN_POSITION)
        self.__health_bar = health_bar.HealthBar(self.__spawn_position, player_constants.HEALTH)
        self.__attacking = False
        img = f'{get_file_path(__file__)}/player/player.webp'
        img_transform = pygame.transform.scale(pygame.image.load(img),
                                              (51, 75)) #image
        self.__image = pygame.transform.flip(img_transform, False, False)
        
        super().__init__(self.__spawn_position, player_constants.HEALTH, player_constants.SPEED)

    @property
    def current_direction(self):
        return self.__current_direction
    
    @current_direction.setter
    def direction(self, val):
        self.__current_direction = val
        
    @property
    def death_player_draw(self):
        return self.__death_player_draw
    
    def attack(self, screen: pygame.Surface) -> None:
        self.__weapon.attack(self)

    def draw_at(self, screen: pygame.Surface, position = None) -> None:
        if self.alive:
            self.set_img_by_direction()
        pos = super().position if position == None else position
        pygame.Surface.blit(screen, self.__image, pos)
        self.__health_bar.draw_at(screen)
        self.__weapon.draw(screen)
        
    def set_img_by_direction(self):
        match self.__current_direction:
            case direction_constants.LEFT:
                self.set_img_draw_left()
            case direction_constants.RIGHT:
                self.set_img_draw_right()
            case _:
                return
        
    def set_img_draw_right(self):
        img = f'{get_file_path(__file__)}/player/player_run.png'
        img_transform = pygame.transform.scale(pygame.image.load(img),
                                              (51, 70)) #image
        self.__image = pygame.transform.flip(img_transform, False, False)
        
    def set_img_draw_left(self):
        img = f'{get_file_path(__file__)}/player/player_run.png'
        img_transform = pygame.transform.scale(pygame.image.load(img),
                                              (51, 70)) #image
        self.__image = pygame.transform.flip(img_transform, True, False)
        
    def draw_at_death(self, screen: pygame.Surface):
        img = f'{get_file_path(__file__)}/player/death_player.png'
        img_transform = pygame.transform.scale(pygame.image.load(img),
                                              (70, 35)) #image
        is_left = self.__current_direction == 'LEFT'
        self.__image = pygame.transform.flip(img_transform, is_left, False)
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

    def run_coin_sound(self) -> None:
        coin_sound = pygame.mixer.Sound(f'{get_file_path(__file__)}/sounds/coin_effect.mp3')
        coin_sound.set_volume(0.5)
        coin_sound.play()
        
        
    def get_power_up(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_p]:
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
                    powerup.activate_power_up()
                    self.run_coin_sound()

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