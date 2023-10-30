from __future__ import annotations

import pygame

from subjects import subject
from constants import powerup_constants


class PowerUpTimerSubject(subject.Subject):
    def __init__(self) -> None:
        self.__event_type = pygame.USEREVENT + 2
        pygame.time.set_timer(self.__event_type, powerup_constants.GENERATE_COOLDOWN)

        super().__init__(self.__event_type)

    def notify_all(self) -> None:
        for callback in super().get_observers():
            callback()

    def handle_events(self) -> None:
        power_up_time_events = pygame.event.get(self.__event_type)

        for _ in range(len(power_up_time_events)):
            self.notify_all()
