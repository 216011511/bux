from fastapi import APIRouter, Depends


# Import paramater models for route
from app.features.song_registration.input import SongRegistrationModel


# Import the services executed by the route
from app.features.song_registration.service import SongRegistration
router = APIRouter()



@router.post("/song_registration", tags=["authentication"])
async def song_registration_api(route_input: SongRegistrationModel):
    return SongRegistration(inputs=route_input).register_song()