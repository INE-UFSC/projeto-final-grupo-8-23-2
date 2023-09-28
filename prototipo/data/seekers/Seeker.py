from abc import abstractmethod, ABC
import Player

class Seeker(ABC):
    def __init__(self,  player_to_chase: Player):
       self.__player_to_chase = player_to_chase
       
    @property
    def player_to_chase(self):
        return self.__player_to_chase

    @player_to_chase.setter
    def player_to_chase(self, val:Player):
        if isinstance(val, Player):
            self.__player_to_chase = val
    
    @abstractmethod
    def chase_player(self) -> None:
        pass
    
    @abstractmethod
    def special_ability(self) -> None:
        pass    