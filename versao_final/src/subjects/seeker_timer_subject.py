from __future__ import annotations

import pygame

from subjects import subject
from constants import seeker_constants


class SeekerTimerSubject(subject.Subject):
    def __init__(self) -> None:
        self.__event_type = pygame.USEREVENT + 1
        pygame.time.set_timer(self.__event_type, seeker_constants.SEEKER_SPAWN_COOLDOWN)

        super().__init__(self.__event_type)

    def notify_all(self) -> None:
        for callback in super().get_observers():
            callback()

    def handle_events(self) -> None:
        seeker_time_events = pygame.event.get(self.__event_type)

        for _ in range(len(seeker_time_events)):
            self.notify_all()

