import pygame

from abc import ABC, abstractmethod
from utils.utils import get_file_path
from utils import utils


class Button(ABC):
    def __init__(self, state) -> None:
        self.__clicked = False
        self.__next_state = state

    def draw_at() -> bool:
        pass
    
    # Getters and Setters

    @property
    def clicked(self) -> bool:
        return self.__clicked
    
    @clicked.setter
    def clicked(self, clicked: bool) -> None:
        if isinstance(clicked, bool):
            self.__clicked = clicked

    @property
    def next_state(self):
        return self.__next_state