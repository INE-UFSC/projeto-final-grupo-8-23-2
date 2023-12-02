from abc import ABC
from constants import img_names_constants, player_constants, seeker_constants, game_constants, weapons_constants
from utils.images.Img import Img
from utils.utils import get_file_path

class ImageGame(ABC):
    def __init__(self) -> None:
        base_path = get_file_path(__file__)
        self.__images:list[Img] = [
            Img(name=img_names_constants.BG_GAME_OVER, path=f"{base_path}/backgrounds/bg_game_over_2.jpg", height=game_constants.SCREEN_HEIGHT, width=game_constants.SCREEN_WIDTH),
            Img(name=img_names_constants.BG_MENU, path=f"{base_path}/backgrounds/menu_background.jpg", height=game_constants.SCREEN_HEIGHT, width=game_constants.SCREEN_WIDTH),
            Img(name=img_names_constants.BG_TUTORIAL, path=f"{base_path}/backgrounds/tutorial_bg.jpg", height=game_constants.SCREEN_HEIGHT, width=game_constants.SCREEN_WIDTH),
            Img(name=img_names_constants.BULLET_FIREBALL, path=f"{base_path}/weapons/fireball.webp", height=15, width=15),
            Img(name=img_names_constants.COIN, path=f"{base_path}/components/coin.webp", height=25, width=25),
            Img(name=img_names_constants.CURSOR, path=f"{base_path}/cursors/white_cursor.webp", height=18, width=18),
            Img(name=img_names_constants.DEATH_PLAYER, path=f"{base_path}/player/death_player.png", height=35, width=70),
            Img(name=img_names_constants.GHOST, path=f"{base_path}/sprites/ghost.webp", height=seeker_constants.SEEKER_HEIGHT, width=seeker_constants.SEEKER_WIDTH),
            Img(name=img_names_constants.PLAYER, path=f"{base_path}/player/player.webp", height=player_constants.HEIGHT, width=player_constants.WIDTH),
            Img(name=img_names_constants.PURPLEGLASS, path=f"{base_path}/textures/purplegrass.webp", height=150, width=150),
            Img(name=img_names_constants.RED_TIMER, path=f"{base_path}/components/red_timer.webp", height=22, width=22),
            Img(name=img_names_constants.RUN_PLAYER, path=f"{base_path}/player/player_run.png", height=player_constants.HEIGHT, width=player_constants.WIDTH),
            Img(name=img_names_constants.TUTORIAL_MODAL, path=f"{base_path}/backgrounds/tutorial.png"),
            Img(name=img_names_constants.WHITE_TIMER, path=f"{base_path}/components/white_timer.webp", height=22, width=22),
            Img(name=img_names_constants.YELLOW_TIMER, path=f"{base_path}/components/yellow_timer.webp", height=22, width=22),
            Img(name=img_names_constants.EARTHQUAKE, path=f"{base_path}/weapons/earthquake.png", height=weapons_constants.EARTHQUAKER_RANGE*2, width=weapons_constants.EARTHQUAKER_RANGE*2),
        ]
        
    @property
    def images(self):
        return self.__images
    
    def get_image(self, name):
        if name in list(map(lambda x: x.name, self.images)):
            for img in self.images:
                if img.name == name:
                    return img
        return None
                    
    def transform_flip(self, name, flip_x=False, flip_y=False):
        if name in list(map(lambda x: x.name, self.images)):
            for img in self.images:
                if img.name == name:
                    return img.transform_flip(flip_x, flip_y)
        return None
    
    def transform_scale(self, name):
        if name in list(map(lambda x: x.name, self.images)):
            for img in self.images:
                if img.name == name:
                    return img.transform_scale()
        return None

    def transform_rotate(self, name, deg:int):
        if name in list(map(lambda x: x.name, self.images)):
            for img in self.images:
                if img.name == name:
                    return img.transform_rotate(deg)
        return None
    
    def transform_scale_2x(self, name):
        if name in list(map(lambda x: x.name, self.images)):
            for img in self.images:
                if img.name == name:
                    return img.transform_scale_2x()
        return None