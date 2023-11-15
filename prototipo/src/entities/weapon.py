from entities.bullet import Bullet

class Weapon:
    def __init__(
            self,
            name: str,
            damage: int,
            range: int,
            sprite: str
        ) -> None:
        self.__name = name
        self.__damage = damage
        self.__range = range
        self.__sprite = sprite
        self.__bullets = []

    def shoot(self, angle, player_x, player_y) -> None:
        bullet = Bullet(angle, 10, player_x, player_y, self.__range)
        self.__bullets.append(bullet)

    def draw(self, screen) -> None:
        for bullet in self.__bullets:
            bullet.draw_at(screen)
            bullet.move()
            if not bullet.moving:
                self.__bullets.remove(bullet)

    # Getters and Setters

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, val:str) -> None:
        if isinstance(val, str):
            self.__name = val

    @property
    def damage(self) -> int:
        return self.__damage

    @damage.setter
    def damage(self, val: int) -> None:
        if isinstance(val, int):
            self.__damage = val

    @property
    def range(self) -> int:
        return self.__range

    @range.setter
    def range(self, val:int) -> None:
        if isinstance(val, int):
            self.__range = val

    @property
    def sprite(self) -> str:
        return self.__sprite

    @sprite.setter
    def sprite(self, val: str) -> None:
        if isinstance(val, str):
            self.__sprite = val

    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets

    @bullets.setter
    def bullets(self, val: list[Bullet]):
        if isinstance(val, list):
            self.__bullets = val