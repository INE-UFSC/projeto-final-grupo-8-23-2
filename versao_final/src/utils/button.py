import pygame
import utils.utils
class Button():
    
    def __init__(self, text, state):
        self.__text = text
        self.__clicked = False
        self.__font = pygame.font.Font('../resources/NightsideDemoRegular.ttf', 36)
        self.__render = self.__font.render(self.__text, True, (255, 255, 255))
        self.__rect = self.__render.get_rect()
        self.__next_state = state
        
    @property
    def next_state(self):
        return self.__next_state
        
    def draw_at(self, surface, x, y):
        self.__rect.topleft = (x, y)
        action = False
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.__clicked:
                action = True
                self.__clicked = True
                self.__render = self.__font.render(self.__text, True, (utils.utils.pink))
                # depois opinem sobre esse ""
            if pygame.mouse.get_pressed()[0] == 0:
                self.__clicked = False
                self.__render = self.__font.render(self.__text, True, (255, 255, 255))
        surface.blit(self.__render, self.__rect.topleft)
        return action

    @property   
    def width(self):
        return self.__rect.width