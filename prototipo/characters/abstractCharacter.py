from abc import ABC, abstractmethod
from data.entities.Weapon import Weapon

class Character(ABC):
    def __init__(self, coordinate_x: int, coordinate_y: int, healt: int, damage: int, speed: int, sprite: str, armor: float, weapon:Weapon):
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y
        self.__healt = healt
        self.__damage = damage
        self.__speed = speed
        self.__sprite = sprite
        self.__armor = armor
        self.__weapon = weapon
    
    @property
    def weapon(self):
        return self.__weapon
    
    @weapon.setter
    def weapon(self, weapon):
        self.__weapon = weapon

    @property
    def coordinate_x(self):
        return self.__coordinate_x
    
    @property
    def coordinate_y(self):
        return self.__coordinate_y

    @property
    def healt(self):
        return self.__healt
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def damage(self):
        return self.__damage
    
    @property
    def sprite(self):
        return self.__sprite

    @property
    def armor(self):
        return self.__armor

    @coordinate_x.setter
    def coordinate_x(self, coordinate_x:int):
        self.__coordinate_x = coordinate_x

    @coordinate_y.setter
    def coordinate_y(self, coordinate_y:int):
        self.__coordinate_y = coordinate_y

    @healt.setter
    def healt(self, healt:int):
        self.__healt = healt

    @damage.setter
    def damage(self, damage:int):
        self.__damage = damage

    @speed.setter
    def speed(self, speed:int):
        self.__speed = speed

    @sprite.setter
    def sprite(self, sprite:str):
        self.__sprite = sprite

    @armor.setter
    def armor(self, armor:float):
        self.__armor = armor

    def move_up(self): # separei o comando move em quatro partes, nao sei se esta na maneira correta mas foi o que fez sentido pra mim.
        self.__coordinate_x += (1 + self.__speed) # coloquei a velocidade como um simples incremento, mas essa formula poderia ser alterada se a jogabilidade nao ficar boa

    def move_down(self):
        self.__coordinate_x -= (1 + self.__speed)
    
    def move_right(self):
        self.__coordinate_y += (1 + self.__speed)

    def move_left(self):
        self.__coordinate_y -= (1 + self.__speed)

    # deixei como abstrato pq o modo de atacar do personagem pode ser diferente
    @abstractmethod
    def attack(self):
        pass
        # for enemy in game.enemy:
        #     if (((enemy.coordinate_x - self.coordinate_x)**2) + ((enemy.coordinate_y - self.coordinate_y)**2))**1/2 <= self.weapon.range:
        #           enemy.healt -= self.weapon.damage
        # ideia de algoritmo para implementar caso o character for o personagem principal

# mudar diagrama:
# move -> move_up, move_down, move_left, move_right
# criacao do self.__weapon