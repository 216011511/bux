from os import access
from app.database import session, Artists, Albums, AlbumAccessMatrix
from app.features.album_registration.input import AlbumRegistrationModel

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy import or_

# TODO: Encrypt user password before storing it in db

class AlbumRegistration:
    ''' 
    How To Register A New Company:
        Check if the unique details do not exist already in the system.
        If they do not exist, add the company to the session link user with 
        company in the company access matrix then commit the session.
    '''

    def __init__(self, inputs: AlbumRegistrationModel):
        self.__inputs = inputs

    def register_album(self):
        album = session.query(Albums).filter_by(
                album_name = self.__inputs.album_name
        ).first()

        if album == None:
            new_album = Albums(
                album_name=self.__inputs.album_name
            )

            access_matrix = AlbumAccessMatrix(
                artist_id=self.__inputs.artist_id,
                record_label=' Young Money'
            )

            new_album.artists.append(access_matrix)
            status_code = 401
            content_msg = ''
            try:
                session.add(new_album)
                session.commit()
                status_code = 201
                content_msg = 'Successful Album Registration'
            except:
                session.rollback()
                status_code = 401
                content_msg = 'Invalid AlbumRegistration'

            finally:
                session.close()

            return JSONResponse(status_code=status_code, content=content_msg)

        raise HTTPException(
            status_code=401, detail='Invalid Album Registration')
