from fastapi import FastAPI

from app.configuration.db import initialize_db
from app.domain.games import Games
from app.domain.islands import Islands
from app.repository.games import Games as GamesRepository
from app.repository.islands import Islands as IslandsRepository
from app.router.games import GamesRouter
from app.router.islands import IslandsRouter

app = FastAPI()

db = initialize_db()
games_repository = GamesRepository(db)
islands_repository = IslandsRepository(db)

games = Games(games_repository)
islands = Islands(islands_repository)

games_router = GamesRouter(games, islands_repository)
islands_router = IslandsRouter(islands)


app.include_router(games_router.router)
app.include_router(islands_router.router)


@app.get("/")
async def root():
    return "Hello! Welcome to evacubanana!"
