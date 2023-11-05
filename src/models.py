import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False, unique=True)
    Name = Column(String(250), nullable= False)
    Lastname = Column(String(250), nullable= False)
    BirthDay = Column(datetime(), default=datetime.now())
    Pasword = Column(String(250), nullable= False)
    Email = Column(String(250), nullable = False, unique= True)

class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(datetime, nullable=False)
    edited = Column(datetime, nullable=False)
    url = Column(String(50), nullable=False)
    
class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, primary_key=True)
    mass = Column(Integer, primary_key=True)
    skin_color = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    created = Column(datetime, nullable=False)
    edited = Column(datetime, nullable=False)
    homeworld = Column(String(250), nullable=False)

    class FavoritePlanets(Base):
      __tablename__ = 'fav_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(Users)
    Favorites = relationship(Planets)

class FavoriteCharacters(Base):
    __tablename__ = 'fav_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(Users)
    Favorites = relationship(Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
