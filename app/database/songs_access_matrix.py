from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base


class SongsAccessMatrix(Base):
    __tablename__ = 'songs_access_matrix'

    artist_id = Column(Integer, ForeignKey('artists.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)

    #Linkng objects 
    song = relationship("Songs", back_populates="artists")    
    artists = relationship("Artists", back_populates="songs")