from pydantic import Field
from pydantic import BaseModel
from typing import Optional, List

from app.domain.models.note import Note


class Game(BaseModel):
    uid: Optional[str] = None
    islandSeed: int = Field(..., example=123)
    score: int = Field(..., example=99)
    username: str = Field(..., example='annterina')
    notes: List[Note] = Field(default_factory=list)
