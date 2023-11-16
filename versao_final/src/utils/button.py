import pygame

from abc import ABC, abstractmethod
from utils.utils import get_file_path
from utils import utils
from states.state import State


class Button(ABC):
    def __init__(self, action) -> None:
        self.__clicking:bool = False
        self.__full_click:bool = False
        self.__next_action = action

    def draw_at() -> bool:
        pass
    
    def change_state(self) -> None:
        pass
    
    # Getters and Setters

    @property
    def clicking(self) -> bool:
        return self.__clicking
    
    @clicking.setter
    def clicking(self, clicking: bool) -> None:
        if isinstance(clicking, bool):
            self.__clicking = clicking

    @property
    def next_action(self):
        return self.__next_action
    
    @property
    def full_click(self) -> bool:
        return self.__full_click
    
    @full_click.setter
    def full_click(self, full_click: bool) -> None:
        if isinstance(full_click, bool):
            self.__full_click = full_click