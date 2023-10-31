import pygame
import math
from constants import game_constants

class Map:
    def __init__(self) -> None:
        self.__size = 100
        self.__image = pygame.transform.scale(pygame.image.load('versao_final/resources/grass.png'), (self.__size, self.__size))
        self.__width = game_constants.SCREEN_WIDTH
        self.__height = game_constants.SCREEN_HEIGHT
        
        
    def draw_background(self, screen):

        tilesX = math.ceil(self.__width / self.__size)
        tilesY = math.ceil(self.__height / self.__size)
    
        for x in range(tilesX):
            for y in range(tilesY):
                screen.blit(self.__image, (x * self.__size, y * self.__size))