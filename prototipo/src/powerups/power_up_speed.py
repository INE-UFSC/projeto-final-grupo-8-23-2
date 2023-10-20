from abc import ABC, abstractmethod
from powerups.power_up import PowerUp
import pygame
import constants.player_constants as playerconst
import constants.powerup_constants as powerconst


class PowerUpSpeed(PowerUp):
    def __init__(self, player):
        super().__init__(player)
        self.color = pygame.Color("purple")
        self.upgrade_value = powerconst.SPEED

    def power_up_logic(self) -> None:
        self.player.speed += self.upgrade_value
