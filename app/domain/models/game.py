from uuid import uuid4

from pydantic import Field, PrivateAttr
from pydantic import BaseModel
from typing import List

from app.domain.models.note import Note


def game_uid():
    return str(uuid4())


class Game(BaseModel):
    _uid: str = PrivateAttr(default_factory=game_uid)
    island_seed: int = Field(..., example=123)
    score: int = Field(..., example=99)
    username: str = Field(..., example='annterina')
    notes: List[Note] = Field(default_factory=list)

    def model_dump(self, **kwargs):
        return {
            'uid': self._uid,
            'island_seed': self.island_seed,
            'score': self.score,
            'username': self.username,
            'notes': list(map(lambda note: note.model_dump(), self.notes))
        }
