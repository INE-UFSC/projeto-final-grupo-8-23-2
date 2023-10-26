from entities.seeker import Seeker
from entities.player import Player
from constants import seeker_constants

class FightSeeker(Seeker):
    def __init__(self, player_ref: Player) -> None:
        super().__init__(
            player_ref,
            seeker_constants.FIGHT_SEEKER_RANGE,
            seeker_constants.FIGHT_SEEKER_HEALTH,
            seeker_constants.FIGHT_SEEKER_SPEED,
            seeker_constants.FIGHT_SEEKER_DAMAGE,
            seeker_constants.FIGHT_SEEKER_ARMOR
        )

    # metodo implementado na classe pai, porem pode sofrer alteracoes
    #def take_damage(self, damage: int) -> None:
    #    pass

    def strong_punch(self) -> None:
        pass
