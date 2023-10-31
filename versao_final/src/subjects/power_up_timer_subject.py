from __future__ import annotations

import pygame

from subjects import subject
from constants import powerup_constants


# Esta classe vai ditar quando um PowerUp deve ser gerado no mapa
class PowerUpTimerSubject(subject.Subject):
    def __init__(self) -> None:
        # Definindo um tipo de evento para essa classe
        self.__event_type = pygame.USEREVENT + 2
        # Dizendo ao pygame qual evento queremos gerar e de quanto em quanto tempo gerar
        pygame.time.set_timer(self.__event_type, powerup_constants.GENERATE_COOLDOWN)

        super().__init__(self.__event_type)

    # Função que notifica os inscritos que este objeto mudou de estado
    def notify_all(self) -> None:
        for callback in super().get_observers():
            callback()

    # Função que lida com os eventos na callback
    def handle_events(self) -> None:
        power_up_time_events = pygame.event.get(self.__event_type)

        for _ in range(len(power_up_time_events)):
            self.notify_all()

