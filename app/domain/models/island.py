from pydantic import Field
from pydantic import BaseModel
from typing import List

from app.domain.models.note import Note
from app.domain.models.score import Score


class Island(BaseModel):
    seed: int = Field(..., example=123)
    notes: List[Note] = Field(default_factory=list)
    top_scores: List[Score] = Field(default_factory=list)
