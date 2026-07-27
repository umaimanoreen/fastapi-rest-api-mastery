from pydantic import BaseModel


class Movie_item(BaseModel):
    name: str
    year: int
    rating: float
