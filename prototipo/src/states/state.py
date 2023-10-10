from __future__ import annotations

from abc import ABC, abstractmethod


# Classe para modelar cada estado do jogo (Menu, Level, GameOver)
class State(ABC):
    # Recebe uma referencia do jogo
    def __init__(self, game_reference) -> None:
        self.__game_reference = game_reference

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
