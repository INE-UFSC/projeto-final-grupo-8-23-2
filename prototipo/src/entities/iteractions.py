from entities.player import Player
import math
from constants.player_constants import all as powerup_constants
from constants.player_constants import all as player_constants


class Iteractions:
    def __init__(self, seekers:list, player:Player, powerups:list, weapons:list) -> None:
        self.__seekers = seekers
        self.__player = player
        self.__powerups = powerups
        self.__weapons = weapons
    
    def get_power_up(self):
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
    
    