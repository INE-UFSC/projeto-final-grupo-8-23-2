class Player:
    def __init__(self, weapon: Weapon, experience: int, level: int, power_ups: list, score: int):
       self.__weapon = weapon
       self.__experience = experience
       self.__level = level
       self.__power_ups = power_ups
       self.__score = score
       
    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, val:Weapon):
        if isinstance(val, Weapon):
            self.__weapon = val

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, val:int):
        if isinstance(val, int):
            self.__experience = val

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, val:int):
        if isinstance(val, int):
            self.__level = val

    @property
    def power_ups(self):
        return self.__power_ups

    @power_ups.setter
    def power_ups(self, val:list):
        if isinstance(val, list):
            self.__power_ups = val

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val:int):
        if isinstance(val, int):
            self.__score = val