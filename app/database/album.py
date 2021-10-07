from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


from . import Base

class Albums(Base):
   
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    album_name = Column(String(225), unique=True)
 
    artists =  relationship("AlbumAccessMatrix", back_populates="album")
    