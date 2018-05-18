#!/usr/bin/python3
'''User class for login'''

import hashlib
import os
#from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class User(Base):
    '''
    class handles all user
    '''

    __tablename__ = 'users'
    username = Column(String(128), nullable=False, primary_key=True)
    token = Column(String(128), nullable=False, primary_key=True)
    secret = Column(String(128), nullable=False, primary_key=True)
