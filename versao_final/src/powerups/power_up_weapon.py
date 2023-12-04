import pygame
import random

from entities.player import Player
import utils.utils as utils
from powerups.power_up import PowerUp
import constants.powerup_constants as powerconst
from weapons import earthquaker, gun
from constants import img_names_constants


class PowerUpWeapon(PowerUp):
    def __init__(self, player_ref:Player):
        self.__player = player_ref
        game_ref = self.__player.weapon.game_ref
        self.__weapon = random.choice([gun.Gun('Pistol', 10, 400, 'pistol.png', game_ref), earthquaker.Earthquaker('Earthquaker', 50, 200, 'grass.png', game_ref)])
        super().__init__(player_ref, img_names_constants.WEAPON_SPRITE, message_modal=f"VOCÊ CAPTUROU A ARMA {self.__weapon.name}")

        self.color = pygame.Color(utils.red)

    def disable_power_up(self):
        pass

    def power_up_logic(self) -> None:
        self.__player.weapon = self.__weapon
