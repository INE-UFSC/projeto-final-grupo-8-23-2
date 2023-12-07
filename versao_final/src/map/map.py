import pygame
import math
from constants import game_constants
from utils.utils import get_file_path
from utils.images.ImageGame import ImageGame
from constants import img_names_constants


class Map:
    def __init__(self) -> None:
        self.__size = 150
        self.__image = ImageGame().transform_scale(img_names_constants.PURPLEGLASS)
        self.__width = game_constants.SCREEN_WIDTH
        self.__height = game_constants.SCREEN_HEIGHT
        
        
    def draw_background(self, screen):

        tilesX = math.ceil(self.__width / self.__size)
        tilesY = math.ceil(self.__height / self.__size)
    
        for x in range(tilesX):
            for y in range(tilesY):
                screen.blit(self.__image, (x * self.__size, y * self.__size))