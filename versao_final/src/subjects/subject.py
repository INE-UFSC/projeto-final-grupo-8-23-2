from __future__ import annotations
from typing import Callable

from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self.__observers: list[Callable] = []

    def subscribe(self, observer_callback: Callable) -> None:
        self.__observers.append(observer_callback)

    def unsubscribe(self, observer_callback: Callable) -> None:
        self.__observers.remove(observer_callback)

    @abstractmethod
    def handle_events(self) -> None:
        pass

    @abstractmethod
    def notify_all(self) -> None:
        pass

    def get_observers(self) -> list[Callable]:
        return self.__observers
