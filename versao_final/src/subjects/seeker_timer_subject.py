from __future__ import annotations

import pygame

from subjects import subject
from constants import seeker_constants

# Esta classe vai ditar quando um Seeker deve ser spawnado
class SeekerTimerSubject(subject.Subject):
    def __init__(self) -> None:
        # Cria um tipo de evento para essa classe
        self.__event_type = pygame.USEREVENT + 1
        # Dizemos ao pygame qual evento queremos gerar (no caso, o que acabou de ser criado)
        # e de quanto em quanto tempo queremos gerar esse evento
        self.__seeker_timer = pygame.time.set_timer(self.__event_type, seeker_constants.SEEKER_SPAWN_COOLDOWN)

        self.__set_timer_to = 0

        super().__init__(self.__event_type)

    # Função que vai notificar os observadores inscritos nesse subject (assunto)
    def notify_all(self) -> None:
        for callback in self.get_observers():
            callback()

    # Lida com os eventos, no caso, vai spawnar um seeker
    def handle_events(self) -> None:
        seeker_time_events = pygame.event.get(self.__event_type)

        for _ in range(len(seeker_time_events)):
            self.notify_all()

    # Esse método vai parar o timer caso o jogo pause, por exemplo
    # Caso o timer já esteja em 0 (pausado), e o método seja chamado
    # novamente o timer volta a contar
    def change_timer_state(self) -> None:
        self.__seeker_timer = pygame.time.set_timer(self.__event_type, self.__set_timer_to)
        if self.__set_timer_to == 0:
            self.__set_timer_to = seeker_constants.SEEKER_SPAWN_COOLDOWN
        else:
            self.__set_timer_to = 0
