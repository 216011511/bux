from pydantic import BaseModel
from typing import List, Optional


class AlbumRegistrationModel(BaseModel):
    artist_id: int
    album_name: str