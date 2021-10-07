from pydantic import BaseModel
from typing import List, Optional


class ArtistRegistrationModel(BaseModel):
    name: str
    gendre: str
    country: str