from abc import ABC, abstractmethod
import pygame
import random
import constants.powerup_constants as cons
import constants.game_constants as gamecons


class PowerUp(ABC):
    def __init__(self, player):
       self.__player = player
       self.__upgrade_value = None
       self.__icon = None
       self.__position = pygame.Vector2(random.randint(0, gamecons.SCREEN_WIDTH), random.randint(0, gamecons.SCREEN_HEIGHT))
       self.__color = None
       self.__actived = False
       self.__width = cons.width

    def add_power_up_to_list(self):
        self.__player.power_ups.append(self)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.__color, self.__position, self.__width)

    def activate_power_up(self) -> None:
        self.__actived = True
        self.__width = 0
        self.power_up_logic()

    @abstractmethod
    def power_up_logic(self) -> None:
        pass

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
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
        self.__icon = icon

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def actived(self):
        return self.__actived

    @actived.setter
    def actived(self, actived):
        self.__actived = actived