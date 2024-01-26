from pydantic import Field
from pydantic import BaseModel


class Note(BaseModel):
    id: int = Field(..., example=101)
    class_: str = Field(..., example='ObjectClass', alias='class')
    text: str = Field(..., example='The sausage is poisonous!')
