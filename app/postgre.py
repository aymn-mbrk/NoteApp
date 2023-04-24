from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func,create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from sqlalchemy_utils import database_exists, create_database
from config import url

import os
import socket

username = 'hime' #os.environ.get('POSTGRES_USER')
pwd = 'hime' #os.environ.get('POSTGRES_PASSWORD')
database = 'note' #os.environ.get("POSTGRE_DB")

port_id = 5432

postgres_host = 'db'
ip_address = socket.gethostbyname(postgres_host)


Base = declarative_base()
url= f'postgresql://{username}:{pwd}@{ip_address}:{port_id}/{database}'
engine = create_engine(f'{url}', echo=True)
Session = sessionmaker()

class Note(Base):
    __tablename__= 'Note'
    id = Column(Integer, primary_key=True)
    data = Column(String(10000))
    date = Column(DateTime(timezone=True), default=func.now()) #func_now() = current date and time 
    user_id = Column(Integer,ForeignKey('Users.id'))

class User(Base):
    __tablename__= 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True) # No user can have the same email than another user
    password = Column(String(150))
    first_name =Column(String(150))
    notes = relationship('Note') 
