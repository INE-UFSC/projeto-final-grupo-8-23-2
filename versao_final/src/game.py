from __future__ import annotations

import pygame

import utils.utils
from entities import player
from states import state, level_state, menu_state
from constants import game_constants
from utils import mouse


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
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

        # Estado atual do jogo. No protótipo só existirá o estado do level
        self.__current_state: state.State = menu_state.MenuState(self)
        #self.__current_state: state.State = level_state.LevelState(self) 
        self.__current_state.entering()

    def run_bg_music(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load('./resources/sounds/background_music.mp3')
        pygame.mixer.music.play()
        
    def run(self) -> None:
        self.run_bg_music()
        # Inicializa o relógio (clock) do jogo
        clock = pygame.time.Clock()

        # MainLoop do jogo
        while self.__running:
            # for para capturar os eventos do jogo, inicialmente pensado para detectar as teclas pressionadas pelo
            # jogador, mas não sei ao certo como isso funciona, vamos descobrindo pelo caminho
            self.__current_state.update()
            for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.__running = False
    
            # Renderização
            self.__current_state.render()
            pygame.display.flip()
            #self.__screen.fill(utils.utils.green)

            # Define o FPS do jogo
            clock.tick(game_constants.FPS)
            
    def get_screen(self) -> pygame.Surface:
        return self.__screen
    
    @property 
    def current_state(self):
        return self.__current_state
    
    @current_state.setter
    def current_state(self, state):
        self.__current_state = state