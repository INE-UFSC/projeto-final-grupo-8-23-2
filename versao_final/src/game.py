from __future__ import annotations

import pygame

import utils.utils
from entities import player
from states import state, menu_state
from constants import game_constants
from utils import mouse


class Game:
    def __init__(self) -> None:
        pygame.init()
        # Atributo para saber se o jogo está rodando
        self.__running = True

        # Inicializa o display
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Muda a aparencia do mouse
        self.__mouse = mouse.Mouse()

        # Dá nome a janela do jogo
        pygame.display.set_caption('Soul Seekers')

        # Provavelmente vamos adicionar mais coisas aqui, como
        # estado atual do jogo e ícone da janela, por exemplo
        # mas isso não faz sentido no momento

        # Estado atual do jogo.
        self.__current_state: state.State = menu_state.MenuState(self)

        self.__current_state.entering()

    # Método de contém todas as chamadas relacionadas a renderização da tela
    def render(self) -> None:
        self.__current_state.render()
        pygame.display.flip()


    def run(self) -> None:
        # Inicializa o relógio (clock) do jogo
        clock = pygame.time.Clock()
        # MainLoop do jogo
        while self.__running:
            # for para capturar os eventos do jogo, inicialmente pensado para detectar as teclas pressionadas pelo
            # jogador, mas não sei ao certo como isso funciona, vamos descobrindo pelo caminho
            self.__current_state.update()
            for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.__current_state.using_esc):
                    self.__running = False
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE):
                    self.__current_state.key_pressed()

            self.render()

            # Define o FPS do jogo
            clock.tick(game_constants.FPS)

    def set_state(self, new_state: state.State) -> None:
        self.__current_state.exiting()
        self.__current_state = new_state
        self.__current_state.entering()
        
    @property
    def screen(self) -> pygame.Surface:
        return self.__screen