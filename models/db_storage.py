#!/usr/bin/python3
'''
Database engine
'''

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models import User

class DBStorage:
    '''
    handles storage of class instances
    '''

def __init__(self):
    '''
    creates the engine self.__engine
    '''
    #testing purposes using localhost
    engine = sqlalchemy.create_engine('mysql://{}:{}@localhost/{}'.format(
        os.environ.get('tweet_user'),
        os.environ.get('tweet_pwd'),
        os.environ.get('twitter_db'))
#    engine.execute("db")
#    engine.execute("USE db")
