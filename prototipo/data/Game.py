import Player, maps, Weapon

class Game:
    def __init__(self, player:Player, enemy:list, map:Map, powerup: list, score:int, weapon:Weapon):
        self.__player = player
        self.__enemy = enemy
        self.__map = map
        self.__powerup = powerup
        self.__score = score
        self.__weapon = weapon
    
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, val):
        self.__player = val
        
    @property
    def enemy(self):
        return self.__enemy

    @enemy.setter
    def enemy(self, val):
        self.__enemy = val
        
    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, val):
        self.__map = val
        
    @property
    def powerup(self):
        return self.__powerup

    @powerup.setter
    def powerup(self, val):
        self.__powerup = val
        
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        self.__score = val
        
    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, val):
        self.__weapon = val