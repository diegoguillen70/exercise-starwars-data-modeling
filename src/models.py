import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

association_table = Table(
    "association_table",
    Base.metadata,
    Column("planets_id", ForeignKey("planets.id")),
    Column("favorites_id", ForeignKey("favorites.id")),
    Column("startships_id", ForeignKey("startships.id")),
    Column("people_id", ForeignKey("people.id")),
)


class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lasttname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    favorites = relationship("Favorites", back_populates="user", uselist=False)


class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    birth_year = Column(String(15), nullable=False)
    eye_color = Column(String(15), nullable=False)
    gender = Column(String(25), nullable=False)
    hair_color = Column(String(15), nullable=False)
    description = Column(String(500), nullable=False)
    startships = Column(String(15), nullable=False)
    home_world = Column(String(20), nullable=False)


class Favorites(Base):
    __tablename__ = "favorites"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favorite_characters = Column(String(200))
    favorite_planets = Column(String(200))
    favorite_startships = Column(String(200))

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorites")

    favorites = relationship("Favorites", secondary=association_table)


class Planets(Base):
    __tablename__ = "planets"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    terrain = Column(String(30), nullable=False)
    gravity = Column(String(3), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(String(250))
    climate = Column(String(30))
    character_id = Column(Integer, ForeignKey("people.id"))
    character = relationship(People)


class Startships(Base):
    __tablename__ = "startships"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    population = Column(String(250))
    atmosphere = Column(String(250))
    character_id = Column(Integer, ForeignKey("people.id"))
    character = relationship(People)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, "diagram.png")
