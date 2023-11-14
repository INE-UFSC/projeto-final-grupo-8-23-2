from __future__ import annotations

import pygame

import game
from states import state, game_over_state
from entities import player
from entities import seeker
from powerups import power_up
from utils import seeker_spawner, power_up_generator, pause
from subjects import seeker_timer_subject, power_up_timer_subject
from map import map
from datetime import datetime
from datetime import timedelta
from utils.utils import get_file_path
from utils.img_button import ImgButton
from constants import game_constants

class LevelState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
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
        
        self.__pausebt = pause.Pause()
        self.__paused = False
        
        super().__init__(game_ref, path_sound, 0.7)

    def entering(self) -> None:
        super().run_bg_sound()
        self.__power_up_time_listener.subscribe(self.__power_up_generator.generate)
        self.__seeker_time_listener.subscribe(self.__seeker_spawner.spawn)

        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [
                self.__power_up_time_listener.event_type,
                self.__seeker_time_listener.event_type,
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
        self.__map.draw_background(super().game_reference.screen)
        if self.__player.alive:
            self.__player.draw_at(super().game_reference.screen)
        else:
            self.__player.draw_at_death(super().game_reference.screen)
            if self.__date_death_state == datetime.min:
                self.run_death_music()
                self.__date_death_state = datetime.now()
                self.__date_death_state_increment = self.__date_death_state
        for seeker in self.__seekers:
            seeker.draw_at(super().game_reference.screen)
            if not self.__paused:
                seeker.move()
        self.__player.weapon.check_target(self.__seekers)
        for powerup in self.__power_ups:
            powerup.draw_at(super().game_reference.screen)
            powerup.add_power_up_to_list()
        if self.__paused:
            self.pause()

        super().mouse.show_mouse(super().game_reference.screen)

    def update(self) -> None:
        if not self.__paused:
            dead_seekers = []
            for seeker in self.__seekers:
                if not seeker.alive:
                    dead_seekers.append(seeker)
            for seeker in dead_seekers:
                self.__seekers.remove(seeker)

            for powerup in self.__power_ups:
                if powerup.actived:
                    self.__power_ups.remove(powerup)

            self.__seeker_time_listener.handle_events()
            self.__power_up_time_listener.handle_events()

            if self.__player.alive:
                self.__player.move()
                
            self.__player.get_power_up()
            self.__player.attack(super().game_reference.screen)
            
            date_sec = self.__date_death_state + timedelta(seconds=100)
            if not self.__player.alive:
                if self.__date_death_state_increment == date_sec:
                    pygame.mixer.music.pause()
                    super().game_reference.set_state(game_over_state.GameOverState(super().game_reference))
                else:
                    self.__date_death_state_increment = self.__date_death_state_increment + timedelta(seconds=1)
        
    def exiting(self) -> None:
        self.__power_up_time_listener.unsubscribe(self.__power_up_generator.generate)
        self.__seeker_time_listener.unsubscribe(self.__seeker_spawner.spawn)

    def pause(self):
        height = self.__pausebt.buttons[0].height
        base = base = (game_constants.SCREEN_HEIGHT - (height * len(self.__pausebt.buttons))) / 2
        
        # arrumar isso aqui depois
        color = (0, 0, 0, 127)
        surface = pygame.Surface(self.__pausebt.bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(surface, color, surface.get_rect())
        super().game_reference.screen.blit(surface, self.__pausebt.bg_rect.topleft)
        
        for button in self.__pausebt.buttons:
            button.draw_at(super().game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base)
            base += self.__pausebt.spacing
            
    def space_pressed(self) -> None:
        self.__paused = not self.__paused