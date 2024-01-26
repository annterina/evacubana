from pydantic import Field
from pydantic import BaseModel


class Note(BaseModel):
    id: int = Field(..., example=101)
    text: str = Field(..., example='The sausage is poisonous!')
