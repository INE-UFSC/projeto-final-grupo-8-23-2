from abc import ABC, abstractmethod
import pygame
import random
from datetime import datetime

import constants.powerup_constants as cons
import constants.game_constants as gamecons
from entities.player import Player
from utils.utils import get_file_path
import time


class PowerUp(ABC):
    def __init__(self, player_ref: Player, contains_timer = True, max_timer_start = 5, message_modal = None) -> None:
       self.__player = player_ref
       self.__upgrade_value = None
       self.__icon = None
       self.__position = self.define_power_up_position()
       self.__color = None
       self.__actived = False
       self.__width = cons.WIDTH
       self.__timer_start = None
       self.__contains_timer = contains_timer
       self.__max_time_sec = max_timer_start
       self.__finished_time = False # tempo esgotado
       self.__finished = False
       
       # tempo que o power up durara na tela
       self.__timer_draw_start = None
       self.__max_time_draw_sec = 10
       self.__hidden_draw = False
       
       self.__timer_modal_start = None
       self.__max_time_modal_sec = 2
       self.__hidden_modal = False
       
       self.__message_modal = message_modal
       
    @property
    def contains_timer(self):
        return self.__contains_timer

    @contains_timer.setter
    def contains_timer(self, val:bool):
        self.__contains_timer = val
        
    @property
    def finished(self):
        return self.__finished

    @finished.setter
    def finished(self, val:bool):
        self.__finished = val
        
    @property
    def hidden_draw(self):
        return self.__hidden_draw

    @hidden_draw.setter
    def hidden_draw(self, val:bool):
        self.__hidden_draw = val
        
    @property
    def hidden_modal(self):
        return self.__hidden_modal

    @hidden_modal.setter
    def hidden_modal(self, val:bool):
        self.__hidden_modal = val
        
    @property
    def finished_time(self):
        return self.__finished_time

    @finished.setter
    def finished_time(self, val:bool):
        self.__finished_time = val

    def define_power_up_position(self) -> pygame.Vector2:
        x = random.randint(cons.WIDTH, gamecons.SCREEN_WIDTH - cons.WIDTH)
        y = random.randint(cons.WIDTH, gamecons.SCREEN_HEIGHT - cons.WIDTH)
        return pygame.Vector2(x, y)
    
    def define_timer_position(self) -> pygame.Vector2:
        return pygame.Vector2(10, 10)

    def add_power_up_to_list(self):
        self.__player.power_ups.append(self)
        
    def counter_time(self, time_start:datetime, max_time_sec):
        sec = 0 
        
        if time_start != None:
            sec = time_start.timestamp() - datetime.now().timestamp()
            double_max_time_sec = max_time_sec * 2
            
            if max_time_sec - int(sec) < double_max_time_sec:
                sec = abs(max_time_sec - abs(int(sec)))
            else:
                sec = 0 
        return sec
    
    def draw_modal_message(self, screen):
        font = pygame.font.Font(f'{get_file_path(__file__)}/fonts/gunmetl.ttf', 40)
        color_text = (153,0,153)
        text_surface = font.render(self.__message_modal, False, color_text)
        text_pos_x = (gamecons.SCREEN_WIDTH / 2) - (text_surface.get_width() / 2)
        text_surface_position = pygame.Vector2(text_pos_x, 20)
    
        if self.__timer_modal_start == None:
            self.__timer_modal_start = datetime.now()
        sec = self.counter_time(self.__timer_modal_start, self.__max_time_modal_sec)
        self.__hidden_modal = sec == 0
        
        pygame.Surface.blit(screen, text_surface, text_surface_position)

    def draw_at(self, screen: pygame.Surface) -> None:
        if not self.actived and not self.hidden_draw:
            img = f'{get_file_path(__file__)}/components/coin.webp'
            img_transform = pygame.transform.scale(pygame.image.load(img),
                                                (25, 25)) #image
            image = pygame.transform.flip(img_transform, True, False)
            
            if self.__timer_draw_start == None:
                self.__timer_draw_start = datetime.now()
            sec = self.counter_time(self.__timer_draw_start, self.__max_time_draw_sec)
            self.__hidden_draw = sec == 0
            pygame.Surface.blit(screen, image, self.__position)
        # pygame.draw.circle(screen, self.__color, self.__position, self.__width)
        
    def draw_timer(self, screen:pygame.Surface):
        # add component img
        if not self.__finished_time:
            img = f'{get_file_path(__file__)}/components/white_timer.webp'
            
            # add temporizador
            pygame.font.init()
            font = pygame.font.Font(f'{get_file_path(__file__)}/fonts/digital-7.ttf', 25)
            color_text = (255,255,255)
            
            sec = self.counter_time(self.__timer_start, self.__max_time_sec)
            self.__finished_time = sec == 0
            
            half_total_sec = int(self.__max_time_sec / 2)
            ending_total_sec = int(self.__max_time_sec * 0.8)
            
            if sec > ending_total_sec:
                color_text = (255,255,255)
            elif ending_total_sec >= sec > half_total_sec:
                color_text = (255,255,0) # yellow
                img = f'{get_file_path(__file__)}/components/yellow_timer.webp'
            else:
                img = f'{get_file_path(__file__)}/components/red_timer.webp'
                color_text = (255,0,0)
                
            txt_sec = f"00:{sec}" if sec > 9 else f"00:0{sec}"
            text_surface = font.render(txt_sec, False, color_text)
            text_surface_position = pygame.Vector2(40, 10)
            
            pygame.Surface.blit(screen, text_surface, text_surface_position)
            
            # renderiza o cronometro
            img_transform = pygame.transform.scale(pygame.image.load(img),
                                                (22, 25)) #image
            image = pygame.transform.flip(img_transform, True, False)
            pygame.Surface.blit(screen, image, self.define_timer_position())
        else:
            self.disable_power_up()

    def activate_power_up(self, screen:pygame.Surface) -> None:
        # p fazer o calculo do timer
        if self.__timer_start == None:
            self.__timer_start = datetime.now()
        self.__actived = True
        self.__width = 0
        self.power_up_logic()

    @abstractmethod
    def disable_power_up(self):
        pass
    
    @abstractmethod
    def power_up_logic(self) -> None:
        pass
    
    # Getters and Setters

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self.__player = player

    @property
    def upgrade_value(self):
        return self.__upgrade_value

    @upgrade_value.setter
    def upgrade_value(self, value):
        self.__upgrade_value = value

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon):
        if isinstance(icon, str):
            self.__icon = icon

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if isinstance(position, pygame.Vector2):
            self.__position = position

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if isinstance(color, str): 
            self.__color = color

    @property
    def actived(self):
        return self.__actived

    @actived.setter
    def actived(self, actived):
        if isinstance(actived, bool):
            self.__actived = actived
