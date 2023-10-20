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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def current_health(self):
        return self.__current_health

    @current_health.setter
    def current_health(self, value):
        self.__current_health = value

    @property
    def max_health(self):
        return self.__max_health

    @max_health.setter
    def max_health(self, value):
        self.__max_health = value
