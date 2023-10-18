import pygame


class HealthBar:
    def __init__(self, bar_position: pygame.Vector2, max_health: int, width=100, height=15) -> None:
        self.__position = bar_position
        self.__width = width
        self.__height = height
        self.__current_health = max_health
        self.__max_health = max_health

    def draw_at(self, surface: pygame.Surface) -> None:
        ratio = self.__current_health / self.__max_health
        pygame.draw.rect(surface, 'red', (self.__position.x - self.__width / 2, self.__position.y + 60, self.__width, self.__height))
        pygame.draw.rect(surface, 'green', (self.__position.x - self.__width / 2, self.__position.y + 60, self.__width * ratio, self.__height))

    def update_health_bar(self, health: int) -> None:
        self.__current_health = health
