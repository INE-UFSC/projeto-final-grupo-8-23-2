from __future__ import annotations

import pygame

from states.state import State
from entities import player
from entities import seeker, fight_seeker
from powerups import power_up, power_up_health, power_up_speed
from utils import seeker_spawner
from subjects import seeker_timer_subject
import game

class LevelState(State):
    def __init__(self, game_ref: game.Game) -> None:
        self.__player: player.Player = player.Player()

        self.__seekers: list[seeker.Seeker] = []

        self.__power_ups: list[power_up.PowerUp] = [power_up_health.PowerUpHealth(self.__player) for _ in range(2)] + [power_up_speed.PowerUpSpeed(self.__player) for _ in range(2)]

        self.__seeker_spawner = seeker_spawner.SeekerSpawner(self.__seekers, self.__player)
        self.__seeker_time_listener = seeker_timer_subject.SeekerTimerSubject()

        super().__init__(game_ref)

    def entering(self) -> None:
        self.__seeker_time_listener.subscribe(self.__seeker_spawner.spawn)

        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [
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
            if not seeker.alive:
                self.__seekers.remove(seeker)
            seeker.draw_at(super().get_game().get_screen())
            seeker.move()
        for powerup in self.__power_ups:
            powerup.draw_at(super().get_game().get_screen())
            powerup.add_power_up_to_list()

    def update(self) -> None:
        self.__seeker_time_listener.handle_events()

        self.__player.move()
        self.__player.get_power_up()
        self.__player.attack(super().get_game().get_screen())

    def exiting(self) -> None:
        return super().exiting()
