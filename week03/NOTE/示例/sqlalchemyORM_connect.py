import pymysql
from sqlalchemy import create_engine, Column, Table, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
'''
使用ORM的四点要求
1. 所有表必需继承自declarative_base对象
2. 创建表时必须有 __tablename__ 的属性
3. 表中要包含一个或多个属性
4. 每表必须要有一个主键
'''


Base = declarative_base()

class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)
    

class Auther_talbe(Base):
    __tablename__ = 'autherorm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

dburl = 'mysql+pymysql://devops:qwe123456@node1:3306/db1?charset=utf8mb4'

engine = create_engine(dburl, echo=True, encoding='utf-8')
print(engine)

Base.metadata.create_all(engine)


'''Out
Engine(mysql+pymysql://devops:***@node1:3306/db1?charset=utf8mb4)
2020-12-11 16:57:22,163 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2020-12-11 16:57:22,164 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,169 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2020-12-11 16:57:22,169 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,174 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
2020-12-11 16:57:22,174 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,176 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
2020-12-11 16:57:22,177 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,184 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
2020-12-11 16:57:22,184 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,188 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
2020-12-11 16:57:22,189 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,193 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
2020-12-11 16:57:22,193 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,216 INFO sqlalchemy.engine.base.Engine DESCRIBE `bookorm`
2020-12-11 16:57:22,220 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,223 INFO sqlalchemy.engine.base.Engine ROLLBACK
2020-12-11 16:57:22,224 INFO sqlalchemy.engine.base.Engine DESCRIBE `autherorm`
2020-12-11 16:57:22,224 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,226 INFO sqlalchemy.engine.base.Engine ROLLBACK
2020-12-11 16:57:22,230 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE bookorm (
        book_id INTEGER NOT NULL AUTO_INCREMENT, 
        book_name VARCHAR(50), 
        PRIMARY KEY (book_id)
)


2020-12-11 16:57:22,231 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,241 INFO sqlalchemy.engine.base.Engine COMMIT
2020-12-11 16:57:22,242 INFO sqlalchemy.engine.base.Engine CREATE INDEX ix_bookorm_book_name ON bookorm (book_name)
2020-12-11 16:57:22,242 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,250 INFO sqlalchemy.engine.base.Engine COMMIT
2020-12-11 16:57:22,253 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE autherorm (
        user_id INTEGER NOT NULL AUTO_INCREMENT, 
        username VARCHAR(15) NOT NULL, 
        created_on DATETIME, 
        updated_on DATETIME, 
        PRIMARY KEY (user_id), 
        UNIQUE (username)
)


2020-12-11 16:57:22,253 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 16:57:22,258 INFO sqlalchemy.engine.base.Engine COMMIT
'''