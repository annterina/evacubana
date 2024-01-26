from fastapi import APIRouter, HTTPException

from app.domain.islands import Islands


class IslandsRouter:
    def __init__(self, islands: Islands) -> None:
        self.__islands = islands

    @property
    def router(self):
        api_router = APIRouter(prefix='/islands', tags=['islands'])

        @api_router.get('/')
        def get_all():
            return self.__islands.get_all()

        @api_router.get('/{seed}')
        def get_game(seed: int):
            try:
                return self.__islands.get_island(seed)
            except KeyError:
                raise HTTPException(status_code=404, detail='Island not found')

        @api_router.get('/random')
        def get_random():
            return self.__islands.get_random()

        return api_router
