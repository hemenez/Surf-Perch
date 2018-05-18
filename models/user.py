#!/usr/bin/python3
'''User class for login'''

import hashlib
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float

class User():
    '''
    class handles all user
    '''

    __tablename__ = 'users'
    username = Column(String(128), nullable=False)
    token = Column(String(128), nullable=False)
    secret = Column(String(128), nullable=False)
