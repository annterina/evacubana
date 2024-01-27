from fastapi import APIRouter, BackgroundTasks

from app.domain.games import Games
from app.domain.islands import Islands
from app.domain.models.game import Game
from app.service.islands_service import update_island_from_game


class GamesRouter:
    def __init__(self, games: Games, islands: Islands) -> None:
        self.__games = games
        self.__islands = islands

    @property
    def router(self):
        api_router = APIRouter(prefix='/games', tags=['games'])

        @api_router.post('/')
        def create_game(game: Game, background_tasks: BackgroundTasks):
            background_tasks.add_task(update_island_from_game, self.__islands, game)
            return self.__games.create_game(game)

        @api_router.get('/')
        def get_all():
            return self.__games.get_all()

        return api_router
