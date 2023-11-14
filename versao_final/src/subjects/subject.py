from __future__ import annotations
from typing import Callable

from abc import ABC, abstractmethod


# Classe que define uma interface para os subjects (assuntos) que serão observados por
# alguma outra classe
class Subject(ABC):
    def __init__(self, event_type: int):
        # Vai guardar o tipo de evento
        self.__event_type = event_type
        # Lista dos observadores desse assunto/subject
        # Esta será uma lista de callables, ou seja, funções
        self.__observers: list[Callable] = []
        self.__paused = False

    # Método para inscrever um observador no subject em questão
    def subscribe(self, observer_callback: Callable) -> None:
        self.__observers.append(observer_callback)

    # Método para desinscrever um observador do subject em questão
    def unsubscribe(self, observer_callback: Callable) -> None:
        self.__observers.remove(observer_callback)
        
    # Abstract Methods

    # Método abstrato para notificar os inscritos que ocorreu um evento
    @abstractmethod
    def notify_all(self) -> None:
        pass

    # Método abstrato que vai lidar com os eventos levantados
    @abstractmethod
    def handle_events(self) -> None:
        pass
    
    # Getters and Setters
    
    @property
    def observers(self) -> list[Callable]:
        return self.__observers
    
    @property
    def event_type(self) -> int:
        return self.__event_type
    
    @property
    def paused(self) -> bool:
        return self.__paused

    @paused.setter
    def paused(self, paused: bool) -> None:
        if isinstance(paused, bool):
            self.__paused = paused