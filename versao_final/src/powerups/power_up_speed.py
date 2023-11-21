import pygame
from entities.player import Player

import utils.utils as utils
from powerups.power_up import PowerUp
import constants.powerup_constants as powerconst


class PowerUpSpeed(PowerUp):
    def __init__(self, player_ref:Player):
        speed_percent = int(abs((powerconst.SPEED * 100 / player_ref.speed_init) - 100))
        super().__init__(player_ref, message_modal=f"SPEED {speed_percent}% AUMENTADA")
        
        print(player_ref.speed_init)
        self.color = pygame.Color(utils.purple)
        self.upgrade_value = powerconst.SPEED

    def disable_power_up(self):
        self.player.speed = self.player.speed_init
        
        self.actived = False
        self.finished = True
        
    def power_up_logic(self) -> None:
        self.player.speed += self.upgrade_value
