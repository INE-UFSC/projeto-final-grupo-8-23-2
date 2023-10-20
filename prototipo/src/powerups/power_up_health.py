from abc import ABC, abstractmethod
from powerups.power_up import PowerUp
import pygame
import constants.player_constants as playerconst
import constants.powerup_constants as powerconst


class PowerUpHealth(PowerUp):
    def __init__(self, player):
        super().__init__(player)
        self.color = pygame.Color("yellow")
        self.upgrade_value = powerconst.HEALTH

    def power_up_logic(self) -> None:
        if self.player.health + self.upgrade_value > playerconst.HEALTH:
            self.player.health = playerconst.HEALTH
        else:
            self.player.health += self.upgrade_value
        self.player.health_bar.update_health_bar(self.player.health)
