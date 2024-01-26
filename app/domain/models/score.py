from pydantic import Field
from pydantic import BaseModel


class Score(BaseModel):
    user: str = Field(..., example='annterina')
    score: int = Field(..., example=100)
