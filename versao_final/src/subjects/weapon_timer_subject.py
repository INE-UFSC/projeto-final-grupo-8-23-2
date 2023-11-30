# from __future__ import annotations

# import pygame

# from subjects import subject
# from constants import powerup_constants

# class WeaponTimerSubject(subject.Subject):
#     def __init__(self) -> None:
#         self.__event_type = pygame.USEREVENT + 2
#         self.__weapon_timer = pygame.time.set_timer(self.__event_type, powerup_constants.GENERATE_COOLDOWN)
        
#         self.__set_timer_to = 0

#         super().__init__(self.__event_type)

#     # Função que notifica os inscritos que este objeto mudou de estado
#     def notify_all(self) -> None:
#         for callback in self.observers:
#             callback()

#     # Função que lida com os eventos na callback
#     def handle_events(self) -> None:
#         weapon_time_events = pygame.event.get(self.__event_type)

#         for _ in range(len(weapon_time_events)):
#             self.notify_all()

#     def change_timer_state(self) -> None:
#         self.__weapon_timer = pygame.time.set_timer(self.__event_type, self.__set_timer_to)
#         if self.__set_timer_to == 0:
#             self.__set_timer_to = powerup_constants.GENERATE_COOLDOWN
#         else:
#             self.__set_timer_to = 0