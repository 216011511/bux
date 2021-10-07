from fastapi import APIRouter, Depends


# Import paramater models for route
from app.features.artist_registration.input import ArtistRegistrationModel


# Import the services executed by the route
from app.features.artist_registration.service import ArtistRegistration
router = APIRouter()



@router.post("/artist_registration", tags=["authentication"])
async def artist_registration_api(reg_artist: ArtistRegistrationModel):
    return ArtistRegistration(reg_artist).register_artist()