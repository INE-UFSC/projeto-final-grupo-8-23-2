import pygame

from abc import ABC, abstractmethod
from utils.utils import get_file_path
from utils import utils


class Button(ABC):
    def __init__(self, state) -> None:
        self.__clicking = False
        self.__full_click = False
        self.__next_state = state

    def draw_at() -> bool:
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
    def next_state(self):
        return self.__next_state
    
    @property
    def full_click(self) -> bool:
        return self.__full_click
    
    @full_click.setter
    def full_click(self, full_click: bool) -> None:
        if isinstance(full_click, bool):
            self.__full_click = full_click