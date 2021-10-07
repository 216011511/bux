from fastapi import APIRouter, Depends


# Import paramater models for route
from app.features.album_registration.input import AlbumRegistrationModel


# Import the services executed by the route
from app.features.album_registration.service import AlbumRegistration
router = APIRouter()



@router.post("/album_registration", tags=["authentication"])
async def album_registration_api(route_input: AlbumRegistrationModel):
    return AlbumRegistration(route_input).register_album()