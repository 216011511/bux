from pydantic import BaseModel
from typing import List, Optional


class SongRegistrationModel(BaseModel):
    album_id: int
    artist_id: int
    name: str