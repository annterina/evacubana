import random

from pydantic import Field, PrivateAttr
from pydantic import BaseModel
from typing import List

from app.domain.models.note import Note
from app.domain.models.score import Score


def island_seed():
    return random.randint(0, 1_000_000)


class Island(BaseModel):
    _seed: int = PrivateAttr(default_factory=island_seed)
    notes: List[Note] = Field(default_factory=list)
    top_scores: List[Score] = Field(default_factory=list)
    _playable = PrivateAttr(default=True)

    def model_dump(self, **kwargs):
        return {
            'seed': self._seed,
            'notes': list(map(lambda note: note.model_dump(), self.notes)),
            'top_scores': list(map(lambda score: score.model_dump(), self.top_scores)),
            'playable': self._playable
        }
