from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

from app.database.artist import Artists
from app.database.album_access_matrix import AlbumAccessMatrix
from app.database.album import Albums
from app.database.songs import Songs
from app.database.songs_access_matrix import SongsAccessMatrix


engine = create_engine('sqlite:///./album_db.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
