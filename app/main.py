from fastapi import FastAPI

from app.configuration.db import initialize_db
from app.domain.games import Games
from app.repository.games import Games as GamesRepository
from app.router.games import GamesRouter


app = FastAPI()

db = initialize_db()
repository = GamesRepository(db)
games = Games(repository)
games_router = GamesRouter(games)

app.include_router(games_router.router)


@app.get("/")
async def root():
    return "Hello! Welcome to evacubanana!"
