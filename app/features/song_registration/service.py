from app.database import session, Songs,Albums
from app.database.songs_access_matrix import SongsAccessMatrix


from app.features.song_registration.input import SongRegistrationModel

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# TODO: Encrypt user password before storing it in db
class SongRegistration:
    ''' 
    How To Register A New User:
        Check if the unique user details do not exist already in the system.
        If they do not exist, add the user to the session then commit the session.
    '''

    def __init__(self, inputs: SongRegistrationModel):
        self.__inputs = inputs

    def register_song(self):
            new_song = Songs(
                album_id=self.__inputs.album_id,
                name=self.__inputs.name
            )
            access_matrix = SongsAccessMatrix(
                artist_id=self.__inputs.artist_id,
            )
            new_song.artists.append(access_matrix)
            session.add(new_song)
            session.commit()
            return JSONResponse(status_code=201, content='Successful Site Registration')
        
