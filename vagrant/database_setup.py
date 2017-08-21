import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = create_engine()

class Restaurant(Base):
    # __tablename is a special variable that will be used to create a table
    __tablename__ = 'restaurant'

class MenuItem(Base):
    __tablename__ = 'menu_item'

#################### insert at the end of the file ############################
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
