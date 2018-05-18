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

    __engine = None
    __session = None

    def __init__(self):
        '''
        creates the engine self.__engine
        '''

        __engine = None
        __session = None

        #testing purposes using localhost
        engine = sqlalchemy.create_engine('mysql://{}:{}@localhost/{}'.format(
            os.environ.get('tweet_user'),
            os.environ.get('tweet_pwd'),
            os.environ.get('twitter_db'))
    '''
    creates the engine self.__engine
    '''
    #testing purposes using localhost
    self.__engine = sqlalchemy.create_engine('mysql://{}:{}@localhost/{}'.format(
        os.environ.get('tweet_user'),
        os.environ.get('tweet_pwd'),
        os.environ.get('twitter_db'))

    def reload(self):
        """
        creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))
