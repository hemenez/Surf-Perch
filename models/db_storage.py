#!/usr/bin/python3
'''
Database engine
'''

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User

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

        #testing purposes using localhost
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            os.getenv('tweet_user'),
            os.getenv('tweet_pwd'),
            os.getenv('twitter_db')), pool_pre_ping=True)

    def reload(self):
        """
        creates all tables in database & session from engine
        """
        User.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def set(self, obj):
        '''
        Adds the object to the current database session.
        Arguments:
            obj: object passed
        '''
        self.__session.add(obj)
