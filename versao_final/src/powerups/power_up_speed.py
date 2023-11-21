import pygame

import utils.utils as utils
from powerups.power_up import PowerUp
import constants.powerup_constants as powerconst


class PowerUpSpeed(PowerUp):
    def __init__(self, player_ref):
        super().__init__(player_ref)
        self.color = pygame.Color(utils.purple)
        self.upgrade_value = powerconst.SPEED

    def disable_power_up(self):
        self.player.speed -= self.upgrade_value
        
        self.actived = False
        self.finished = True
        
    def power_up_logic(self) -> None:
        self.player.speed += self.upgrade_value
