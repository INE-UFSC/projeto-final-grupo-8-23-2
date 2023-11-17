from weapons.ammo import Ammo


class Earthquake(Ammo):
    def __init__(self, x, y, range) -> None:
        super().__init__(x, y, range)

    def draw_at(self):
        return super().draw()
