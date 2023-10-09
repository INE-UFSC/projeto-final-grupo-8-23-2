class Weapon:
    def __init__(self, name: str, damage: int, range: int, sprite: str):
       self.__name = name
       self.__damage = damage
       self.__range = range
       self.__sprite = sprite
       
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val:str):
        if isinstance(val, str):
            self.__name = val

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, val:int):
        if isinstance(val, int):
            self.__damage = val

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, val:int):
        if isinstance(val, int):
            self.__range = val

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, val:str):
        if isinstance(val, str):
            self.__sprite = val
            
    def shoot(self) -> None:
        pass