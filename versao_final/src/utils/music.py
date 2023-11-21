from utils.sound import Sound
from constants import names_musics
from utils.utils import get_file_path
from abc import ABC

class Music(ABC):
    def __init__(self) -> None:
        base_path = get_file_path(__file__)
        Sound(names_musics.COIN, f"{base_path}path")
        self.__sounds:list[Sound] = [Sound(names_musics.GAME_OVER, f"{base_path}/sounds/game_over_menu_sound.mp3"), 
                                     Sound(names_musics.COIN, f"{base_path}/sounds/coin_effect.mp3", 0.5, False), 
                                     Sound(names_musics.MENU, f"{base_path}/sounds/menu_sound.mp3", 0.4), 
                                     Sound(names_musics.LEVEL, f"{base_path}/sounds/game_sound.mp3"), 
                                     Sound(names_musics.DEATH, f"{base_path}/sounds/death_player.mp3"), 
                                     Sound(names_musics.GAME_OVER_MENU, f"{base_path}/sounds/game_over_menu_sound.mp3"), 
                                     Sound(names_musics.TUTORIAL, f"{base_path}/sounds/tutorial_sound.mp3", 0.4)]
        
    @property
    def sounds(self):
        return self.__sounds
                    
    def run_sound(self, name):
        if name in list(map(lambda x: x.name, self.__sounds)):
            for sound in self.__sounds:
                if sound.name == name:
                    sound.run()