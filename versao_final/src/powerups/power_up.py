from abc import ABC, abstractmethod
import pygame
import random
from datetime import datetime, timedelta

import constants.powerup_constants as cons
import constants.game_constants as gamecons
from constants import img_names_constants
from entities.player import Player
from utils.images.ImageGame import ImageGame
from utils.utils import get_file_path
import utils.utils
import time


class PowerUp(ABC):
    def __init__(self, player_ref: Player, sprite: str, contains_timer = True, max_timer_start = 5, message_modal = None) -> None:
        self.__player = player_ref
        self.__upgrade_value = None
        self.__icon = None
        self.__position = self.define_power_up_position()
        self.__color = None
        self.__actived = False
        self.__timer_start = None
        self.__contains_timer = contains_timer
        self.__max_time_sec = max_timer_start
        self.__current_timer = None # decrescente
        self.__finished_time = False # tempo esgotado
        self.__finished = False
        self.__sprite_name = sprite

        # tempo que o power up durara na tela
        self.__timer_draw_start = datetime.now()
        self.__current_timer_draw = datetime.now()
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
    
    def counter_time(self, time_start:datetime, max_time_sec, current_timer = None):
        sec = 0 
        if current_timer == None:
            current_timer = datetime.now()
        if time_start != None:
            sec = time_start.timestamp() - current_timer.timestamp()
            double_max_time_sec = max_time_sec * 2
            
            if max_time_sec - int(sec) < double_max_time_sec:
                sec = abs(max_time_sec - abs(int(sec)))
            else:
                sec = 0 
        return sec
    
    def update_timer(self,current_timer, sum_microsec):
        return current_timer + timedelta(microseconds=sum_microsec)
    
    def draw_modal_message(self, screen):
        font = pygame.font.Font(f'{get_file_path(__file__)}/fonts/VT323-Regular.ttf', 50)
        color_text = utils.utils.white
        text_surface = font.render(self.__message_modal, False, color_text)
        text_pos_x = (gamecons.SCREEN_WIDTH / 2) - (text_surface.get_width() / 2)
        text_surface_position = pygame.Vector2(text_pos_x, ((gamecons.SCREEN_HEIGHT / 2) - (text_surface.get_height() / 2)))
    
        if self.__timer_modal_start == None:
            self.__timer_modal_start = datetime.now()
        sec = self.counter_time(self.__timer_modal_start, self.__max_time_modal_sec)
        self.__hidden_modal = sec == 0
        
        pygame.Surface.blit(screen, text_surface, text_surface_position)

    def draw_at(self, screen: pygame.Surface, pause_game) -> None:
        if not self.actived and not self.hidden_draw:
            image = ImageGame().transform_flip(self.__sprite_name)

            if not pause_game:
                if self.__current_timer_draw != None:
                    self.__current_timer_draw = self.update_timer(self.__current_timer_draw, 10000)
                    
                sec = self.counter_time(self.__timer_draw_start, self.__max_time_draw_sec, self.__current_timer_draw)
                self.__hidden_draw = sec == 0
            pygame.Surface.blit(screen, image, self.__position)
        # pygame.draw.circle(screen, self.__color, self.__position, self.__width)
        
    def draw_timer(self, screen:pygame.Surface, pause_game):
        # add component img
        if not self.__finished_time:
            if self.__current_timer == None:
                self.__current_timer = datetime.now()
            elif not pause_game:
                self.__current_timer = self.update_timer(self.__current_timer, 10000)
                
            img_transform = ImageGame().transform_scale(img_names_constants.WHITE_TIMER)
            
            # add temporizador
            pygame.font.init()
            font = pygame.font.Font(f'{get_file_path(__file__)}/fonts/digital-7.ttf', 25)
            color_text = (255,255,255)
            
            # if not pause_game:
            sec = self.counter_time(self.__timer_start, self.__max_time_sec, self.__current_timer)
            self.__finished_time = sec == 0
            
            half_total_sec = int(self.__max_time_sec / 2)
            ending_total_sec = int(self.__max_time_sec * 0.8)
            
            if sec > ending_total_sec:
                color_text = (255,255,255)
            elif ending_total_sec >= sec > half_total_sec:
                color_text = (255,255,0) # yellow
                img_transform = ImageGame().transform_scale(img_names_constants.YELLOW_TIMER)
            else:
                img_transform = ImageGame().transform_scale(img_names_constants.RED_TIMER)
                color_text = (255,0,0)
                
            txt_sec = f"00:{sec}" if sec > 9 else f"00:0{sec}"
            text_surface = font.render(txt_sec, False, color_text)
            text_surface_position = pygame.Vector2(40, 10)
            
            pygame.Surface.blit(screen, text_surface, text_surface_position)
            
            # renderiza o cronometro
            pygame.Surface.blit(screen, img_transform, self.define_timer_position())
        else:
            self.disable_power_up()

    def activate_power_up(self, screen:pygame.Surface) -> None:
        # p fazer o calculo do timer
        if self.__timer_start == None:
            self.__timer_start = datetime.now()
        self.__actived = True
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
