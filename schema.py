from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey

Base = declarative_base()


class FollowersActive(Base):

    __tablename__ = 'followers_active'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_profile_api = Column(Integer, ForeignKey('profiles_api.id'), nullable=False)
    id_profile_users = Column(Integer, ForeignKey('profiles_users.id'), nullable=False)
    #time


class ProfilesApi(Base):

    __tablename__ = 'profiles_api'

    id = Column(Integer, primary_key=True, autoincrement=True)
    twitter_handle = Column(String(100), unique=True,  nullable=False)
    key_consumer = Column(String(100), nullable=False)
    secret_consumer = Column(String(100), nullable=False)
    key_access = Column(String(100), nullable=False)
    secret_access = Column(String(100), nullable=False)


class ProfilesUsers(Base):

    __tablename__ = 'profiles_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, primary_key=True)
