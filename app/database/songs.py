from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from . import Base

class Songs(Base):
    
    __tablename__ = 'songs'

    album_id = Column(Integer, ForeignKey('albums.id'))
    id = Column(Integer, primary_key=True)
    name = Column(String(225))

    artists =  relationship("SongsAccessMatrix", back_populates="song")