from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

from . import Base

class Artists(Base):

    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), unique=True)
    gendre = Column(String(45))
    country = Column(String(255))

    # relationships
    albums =  relationship("AlbumAccessMatrix", back_populates="artists")
    songs =  relationship("SongsAccessMatrix", back_populates="artists")