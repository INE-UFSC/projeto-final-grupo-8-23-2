from abc import abstractmethod, ABC

class Character(ABC):
    def __init__(self, coordinate_x: int, coordinate_y: int, health: int, damage: int, speed: int, sprite: str, armor: float):
       self.__coordinate_x = coordinate_x
       self.__coordinate_y = coordinate_y
       self.__health = health
       self.__damage = damage
       self.__speed = speed
       self.__sprite = sprite
       self.__armor = armor
    @property
    def coordinate_x(self):
        return self.__coordinate_x

    @coordinate_x.setter
    def coordinate_x(self, val:int):
        if isinstance(val, int):
            self.__coordinate_x = val

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @coordinate_y.setter
    def coordinate_y(self, val:int):
        if isinstance(val, int):
            self.__coordinate_y = val

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, val:int):
        if isinstance(val, int):
            self.__health = val

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, val:int):
        if isinstance(val, int):
            self.__damage = val

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val:int):
        if isinstance(val, int):
            self.__speed = val

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, val:str):
        if isinstance(val, str):
            self.__sprite = val

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, val:float):
        if isinstance(val, float):
            self.__armor = val
            
    @abstractmethod
    def move() -> None:
        pass
    
    @abstractmethod
    def attack() -> None:
        pass