from entities.bullet import Bullet

class Weapon:
    def __init__(self, name: str, damage: int, range: int, sprite: str):
       self.__name = name
       self.__damage = damage
       self.__range = range
       self.__sprite = sprite
       self.__bullets = []
       
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

    @property
    def bullets(self):
        return self.__bullets
    
    @bullets.setter
    def bullets(self, val:list):
        if isinstance(val, list):
            self.__bullets = val
            
    def shoot(self, angle, player_x, player_y):
        bullet = Bullet(angle, 10, player_x, player_y, self.__range)
        self.__bullets.append(bullet)

    def draw(self, screen):
        for bullet in self.__bullets:
            bullet.draw_at(screen)
            bullet.move()
            if not bullet.moving:
                self.__bullets.remove(bullet)