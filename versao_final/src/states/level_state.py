from __future__ import annotations

import pygame

import game
from states import state, game_over_state
from entities import player
from entities import seeker
from powerups import power_up
from utils import seeker_spawner, power_up_generator
from subjects import seeker_timer_subject, power_up_timer_subject
from map import map
from datetime import datetime
from datetime import timedelta
from utils.utils import get_file_path

class LevelState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        # TODO: Quando o usuário morre, vai para o menu_state e clica em jogar novamente
        # o Player está nascendo no mesmo local em que morreu na partida passada.
        self.__player: player.Player = player.Player()

        self.__seekers: list[seeker.Seeker] = []

        self.__power_ups: list[power_up.PowerUp] = []

        self.__seeker_spawner = seeker_spawner.SeekerSpawner(self.__seekers, self.__player)
        self.__seeker_time_listener = seeker_timer_subject.SeekerTimerSubject()

        self.__power_up_generator = power_up_generator.PowerUpGenerator(self.__power_ups, self.__player)
        self.__power_up_time_listener = power_up_timer_subject.PowerUpTimerSubject()

        self.__map = map.Map()
        
        self.__date_death_state = datetime.min
        self.__date_death_state_increment = self.__date_death_state
        
        path_sound = f'{get_file_path(__file__)}/sounds/game_sound.mp3'
        super().__init__(game_ref, path_sound, 0.1)

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
        
    def run_death_music(self):
        pygame.mixer.music.pause()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load(f"{get_file_path(__file__)}/sounds/death_player.mp3")
        pygame.mixer.music.play()

    def render(self) -> None:
        self.__map.draw_background(super().get_game().get_screen())
        if self.__player.alive:
            self.__player.draw_at(super().get_game().get_screen())
        else:
            self.__player.draw_at_death(super().get_game().get_screen())
            if self.__date_death_state == datetime.min:
                self.run_death_music()
                self.__date_death_state = datetime.now()
                self.__date_death_state_increment = self.__date_death_state
            
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
        super().mouse.show_mouse(super().get_game().get_screen())

    def update(self) -> None:
        dead_seekers = []
        for seeker in self.__seekers:
            if not seeker.alive:
                dead_seekers.append(seeker)
        for seeker in dead_seekers:
            self.__seekers.remove(seeker)

        self.__seeker_time_listener.handle_events()
        self.__power_up_time_listener.handle_events()

        if self.__player.alive:
            self.__player.move()
            
        self.__player.get_power_up()
        self.__player.attack(super().get_game().get_screen())
        
        date_sec = self.__date_death_state + timedelta(seconds=100)
        if not self.__player.alive:
            if self.__date_death_state_increment == date_sec:
                pygame.mixer.music.pause()
                super().get_game().set_state(game_over_state.GameOverState(super().get_game()))
            else:
                self.__date_death_state_increment = self.__date_death_state_increment + timedelta(seconds=1)
        
    def exiting(self) -> None:
        self.__power_up_time_listener.unsubscribe(self.__power_up_generator.generate)
        self.__seeker_time_listener.unsubscribe(self.__seeker_spawner.spawn)
