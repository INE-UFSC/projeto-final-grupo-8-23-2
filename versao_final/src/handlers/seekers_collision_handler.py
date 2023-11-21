from entities import player


class SeekersCollisionHandler:
    def __init__(self, player_ref: player.Player) -> None:
        self.__player_ref = player

    def handle_collision(self, collisions: dict) -> None:

        for seeker1, seeker2 in collisions.items():
            