from __future__ import annotations

import pygame

import utils
from entities import player
from states import state, level_state
from constants import game_constants
# 

class Game:

    def __init__(self) -> None:
        pygame.init()
        # Atributo para saber se o jogo está rodando
        self.__running = True

        # Inicializa o display
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Dá nome a janela do jogo
        pygame.display.set_caption('Soul Seekers')

        # Provavelmente vamos adicionar mais coisas aqui, como
        # estado atual do jogo e ícone da janela, por exemplo
        # mas isso não faz sentido no momento

        # Estado atual do jogo. No protótipo só existirá o estado do level
        self.__current_state: state.State = level_state.LevelState(self)

    def run(self) -> None:
        # Inicializa o relógio (clock) do jogo
        clock = pygame.time.Clock()

        # MainLoop do jogo
        while self.__running:
            # for para capturar os eventos do jogo, inicialmente pensado para detectar as teclas pressionadas pelo
            # jogador, mas não sei ao certo como isso funciona, vamos descobrindo pelo caminho
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.__running = False
            # Preenche a tela com uma cor
            self.__screen.fill(utils.green)
            # Renderizando os objetos do estado, no caso, somente o Player, por enquanto
            self.__current_state.render()

            # Atualiza a tela
            pygame.display.flip()

            # Define o FPS do jogo
            clock.tick(game_constants.FPS)

    def get_screen(self) -> pygame.Surface:
        return self.__screen
