from __future__ import annotations

import pygame

import game
from weapons import gun, earthquaker
from handlers import bullet_collision_handler
from handlers import collision_detector
from utils import seeker_spawner, power_up_generator, pause, utils
from subjects import seeker_timer_subject, power_up_timer_subject
from states import state, game_over_state, menu_state
from datetime import datetime, timedelta
from utils.utils import get_file_path
from constants import game_constants
from entities import player, seeker
from powerups import power_up
from map import map


class LevelState(state.State):
    def __init__(self, game_ref: game.Game) -> None:
        self.__weapon = earthquaker.Earthquaker('Earthquaker', 50, 200, 'grass.png', game_ref)
        # self.__weapon = gun.Gun('Pistol', 10, 400, 'pistol.png', game_ref)
        self.__seekers: list[seeker.Seeker] = []
        self.__power_ups: list[power_up.PowerUp] = []
        self.__player: player.Player = player.Player(self.__weapon)

        self.__bullet_seeker_collision_detector = collision_detector.CollisionDetector(self.__player.weapon.bullets, self.__seekers)
        self.__bullet_seeker_collision_handler = bullet_collision_handler.BulletCollisionHandler(self.__player.weapon, self.__seekers)

        self.__seeker_spawner = seeker_spawner.SeekerSpawner(self.__seekers, self.__player)
        self.__seeker_time_listener = seeker_timer_subject.SeekerTimerSubject()

        self.__power_up_generator = power_up_generator.PowerUpGenerator(self.__power_ups, self.__player)
        self.__power_up_time_listener = power_up_timer_subject.PowerUpTimerSubject()
        self.__map = map.Map()

        self.__date_death_state = datetime.min
        self.__date_death_state_increment = self.__date_death_state

        path_sound = f'{get_file_path(__file__)}/sounds/game_sound.mp3'

        self.__pause_class = pause.Pause()
        self.__paused = False

        super().__init__(game_ref, path_sound, 0.5, using_esc=True)

    def entering(self) -> None:
        self.run_bg_sound()
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
        self.__map.draw_background(self.game_reference.screen)
        if self.__player.alive:
            self.__player.draw_at(self.game_reference.screen)
        else:
            self.__player.draw_at_death(self.game_reference.screen)
            if self.__date_death_state == datetime.min:
                self.run_death_music()
                self.__date_death_state = datetime.now()
                self.__date_death_state_increment = self.__date_death_state
        for seeker in self.__seekers:
            self.__player.weapon.check_target(seeker)
            seeker.draw_at(super().game_reference.screen)
            if not self.__paused:
                seeker.move()
        for powerup in self.__power_ups:
            powerup.draw_at(self.game_reference.screen, self.__paused)
            if powerup.actived and powerup.contains_timer:
                powerup.draw_timer(self.game_reference.screen, self.__paused)
            if powerup.actived and not powerup.hidden_modal:
                powerup.draw_modal_message(self.game_reference.screen)
            powerup.add_power_up_to_list()
        if self.__paused:
            self.pause()
            
        self.mouse.show_mouse(self.game_reference.screen)


    def update(self) -> None:
        if not self.__paused:
            bullet_seeker_collisions = self.__bullet_seeker_collision_detector.detect_collision()
            self.__bullet_seeker_collision_handler.handle_collision(bullet_seeker_collisions)

            dead_seekers = []
            for seeker in self.__seekers:
                if not seeker.alive:
                    dead_seekers.append(seeker)
            for seeker in dead_seekers:
                self.__player.score += seeker.worth_points
                self.__seekers.remove(seeker)

            for powerup in self.__power_ups:
                if powerup.finished:
                    self.__power_ups.remove(powerup)

            self.__seeker_time_listener.handle_events()
            self.__power_up_time_listener.handle_events()

            if self.__player.alive:
                self.__player.move()
            
            self.__player.get_power_up(self.game_reference.screen)
            self.__player.attack(self.game_reference.screen)

            date_sec = self.__date_death_state + timedelta(seconds=100)
            if not self.__player.alive:
                if self.__date_death_state_increment == date_sec:
                    pygame.mixer.music.pause()
                    self.game_reference.set_state(game_over_state.GameOverState(self.game_reference))
                else:
                    self.__date_death_state_increment = self.__date_death_state_increment + timedelta(seconds=1)

    def exiting(self) -> None:
        self.__power_up_time_listener.unsubscribe(self.__power_up_generator.generate)
        self.__seeker_time_listener.unsubscribe(self.__seeker_spawner.spawn)

    def pause(self):
        height = self.__pause_class.buttons[0].height
        base = base = (game_constants.SCREEN_HEIGHT - (height * len(self.__pause_class.buttons))) / 2

        # arrumar isso aqui depois
        color = utils.pink_low_alpha
        surface = pygame.Surface(self.__pause_class.bg_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(surface, color, surface.get_rect())
        self.game_reference.screen.blit(surface, self.__pause_class.bg_rect.topleft)

        for button in self.__pause_class.buttons:
            button.draw_at(self.game_reference.screen, (game_constants.SCREEN_WIDTH - button.width)//2, base)
            base += self.__pause_class.spacing
            if button.full_click:
                getattr(self, button.next_action, None)()  # Obtém a função associada pelo nome

    def key_pressed(self) -> None:
        self.__power_up_time_listener.change_timer_state()
        self.__seeker_time_listener.change_timer_state()
        self.__paused = not self.__paused

    # funções para os botões

    def resume_game(self):
        self.key_pressed()

    def change_to_menu(self):
        self.game_reference.set_state(menu_state.MenuState(self.game_reference))

    def quit_game(self):
        pygame.quit()
        quit()

