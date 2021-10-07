from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base


class AlbumAccessMatrix(Base):
    __tablename__ = 'album_access_matrix'

    artist_id = Column(Integer, ForeignKey('artists.id'), primary_key=True)
    album_id = Column(Integer, ForeignKey('albums.id'), primary_key=True)
    record_label = Column(String(45))
 
    album = relationship("Albums", back_populates="artists")    
    artists = relationship("Artists", back_populates="albums")