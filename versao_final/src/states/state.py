from __future__ import annotations

from abc import ABC, abstractmethod
import game
import pygame
from utils import mouse

# Classe para modelar cada estado do jogo (Menu, Level, GameOver)
class State(ABC):
    # Recebe uma referencia do jogo
    def __init__(self, game_reference: game.Game, path_sound=None, volumn_sound=1, using_esc=False) -> None:
        self.__game_reference = game_reference
        self.__mouse = mouse.Mouse()
        self.__path_sound = path_sound
        self.__sound_volume = volumn_sound
        self.__using_esc = using_esc

    def run_bg_sound(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.__sound_volume)
        pygame.mixer.music.load(self.__path_sound)
        pygame.mixer.music.play(-1)

    # Abstract Methods

    # Método chamado ao entrar em um estado
    @abstractmethod
    def entering(self) -> None:
        pass

    # Método para renderizar a tela do estado
    @abstractmethod
    def render(self) -> None:
        pass

    # Método para atualizar os objetos da tela a cada frame
    @abstractmethod
    def update(self) -> None:
        pass

    # Método para sair de cada estado e garantir que seus assets sejam corretamente fechados, por exemplo
    @abstractmethod
    def exiting(self) -> None:
        pass
    
    # Getters and Setters
    
    @property
    def using_esc(self):
        return self.__using_esc
    
    @property
    def mouse(self):
        return self.__mouse

    @property
    def game_reference(self):
        return self.__game_reference
    
    @game_reference.setter
    def game_reference(self, game_reference):
        self.__game_reference = game_reference
    
    # Funcao generica para evitar erros

    def key_pressed(self) -> None:
        pass
