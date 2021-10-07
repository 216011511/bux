from app.database import session, Artists

from app.features.artist_registration.input import ArtistRegistrationModel

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# TODO: Encrypt user password before storing it in db
class ArtistRegistration:
    ''' 
    How To Register A New User:
        Check if the unique user details do not exist already in the system.
        If they do not exist, add the user to the session then commit the session.
    '''

    def __init__(self, inputs: ArtistRegistrationModel):
        self.__inputs = inputs

    def register_artist(self):
        artist = session.query(Artists).filter_by(
            name = self.__inputs.name
        ).first()

        # If there is no user already in the system that is using the email
        if artist == None:
            new_artist = Artists(
                name=self.__inputs.name,
                gendre=self.__inputs.gendre,
                country=self.__inputs.country
            )
            session.add(new_artist)
            session.commit()
            return JSONResponse(status_code=201, content='Successful Artist Registration')
        
        raise HTTPException(status_code=401, detail='Invalid Artist Registration') 