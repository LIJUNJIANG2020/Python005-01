import pymysql
from sqlalchemy import create_engine, Column, Table, Integer, String, MetaData, ForeignKey, DateTime,Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True) 
    name = Column(String(64))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete='CASCADE'))
    star = Column(Integer)
    comm = Column(Text)

dburl = 'mysql+pymysql://devops:qwe123456@node1:3306/db1?charset=utf8mb4'
engine = create_engine(dburl, echo=True, encoding='utf-8')
Base.metadata.create_all(engine)