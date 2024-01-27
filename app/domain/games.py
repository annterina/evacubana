from uuid import uuid4

from app.domain.models.game import Game
from app.repository.games import Games as GamesRepository


class Games:
    def __init__(self, repository: GamesRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_game(self, uid: str):
        return self.__repository.get_game(uid)

    def create_game(self, game: Game):
        return self.__repository.create_game(game.model_dump())
