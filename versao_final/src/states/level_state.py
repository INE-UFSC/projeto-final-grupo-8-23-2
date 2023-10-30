from __future__ import annotations

import pygame

import game
from states.state import State
from entities import player
from entities import seeker
from powerups import power_up
from utils import seeker_spawner, power_up_generator
from subjects import seeker_timer_subject, power_up_timer_subject


class LevelState(State):
    def __init__(self, game_ref: game.Game) -> None:
        self.__player: player.Player = player.Player()

        self.__seekers: list[seeker.Seeker] = []

        self.__power_ups: list[power_up.PowerUp] = []

        self.__seeker_spawner = seeker_spawner.SeekerSpawner(self.__seekers, self.__player)
        self.__seeker_time_listener = seeker_timer_subject.SeekerTimerSubject()

        self.__power_up_generator = power_up_generator.PowerUpGenerator(self.__power_ups, self.__player)
        self.__power_up_time_listener = power_up_timer_subject.PowerUpTimerSubject()

        super().__init__(game_ref)

    def entering(self) -> None:
        self.__power_up_time_listener.subscribe(self.__power_up_generator.generate)
        self.__seeker_time_listener.subscribe(self.__seeker_spawner.spawn)

        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [
                self.__power_up_time_listener.get_event_type(),
                self.__seeker_time_listener.get_event_type(),
                pygame.KEYDOWN
            ]
        )

    def render(self) -> None:
        self.__player.draw_at(super().get_game().get_screen())
        for seeker in self.__seekers:
            for bullet in self.__player.weapon.bullets:
                if seeker.position[0] - seeker.radius <= bullet.position[0] <= seeker.position[0] + seeker.radius and seeker.position[1] - seeker.radius <= bullet.position[1] <= seeker.position[1] + seeker.radius:
                    seeker.take_damage(self.__player.weapon.damage)
                    bullet.moving = False
            seeker.draw_at(super().get_game().get_screen())
            seeker.move()
        for powerup in self.__power_ups:
            powerup.draw_at(super().get_game().get_screen())
            powerup.add_power_up_to_list()

    def update(self) -> None:
        dead_seekers = []
        for seeker in self.__seekers:
            if not seeker.alive:
                dead_seekers.append(seeker)
        for seeker in dead_seekers:
            self.__seekers.remove(seeker)

        self.__seeker_time_listener.handle_events()
        self.__power_up_time_listener.handle_events()

        self.__player.move()
        self.__player.get_power_up()
        self.__player.attack(super().get_game().get_screen())

    def exiting(self) -> None:
        return super().exiting()
