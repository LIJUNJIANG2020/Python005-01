import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData

# echo=True  开启调试
engine = create_engine('mysql+pymysql://devops:qwe123456@node1:3306/testdb1', echo=True)
# print(engine) # Out: Engine(mysql+pymysql://devops:***@node1:3306/db1)

# 创建元数据
metadata = MetaData(engine)

book_table = Table('book', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )

author_table = Table('author', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', ForeignKey('book.id')),
    Column('author_name', String(128), nullable=False),
    )

try:
    metadata.create_all()
except Exception as e: 
    print(f'Create error {e}')

########################
'''Out:
2020-12-11 15:59:26,840 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2020-12-11 15:59:26,841 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,846 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2020-12-11 15:59:26,846 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,849 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
2020-12-11 15:59:26,849 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,853 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
2020-12-11 15:59:26,853 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,856 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
2020-12-11 15:59:26,856 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,859 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
2020-12-11 15:59:26,859 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,861 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
2020-12-11 15:59:26,861 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,879 INFO sqlalchemy.engine.base.Engine DESCRIBE `book`
2020-12-11 15:59:26,879 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,883 INFO sqlalchemy.engine.base.Engine ROLLBACK
2020-12-11 15:59:26,885 INFO sqlalchemy.engine.base.Engine DESCRIBE `author`
2020-12-11 15:59:26,885 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,916 INFO sqlalchemy.engine.base.Engine ROLLBACK
2020-12-11 15:59:26,918 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE book (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        name VARCHAR(20), 
        PRIMARY KEY (id)
)


2020-12-11 15:59:26,918 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,929 INFO sqlalchemy.engine.base.Engine COMMIT
2020-12-11 15:59:26,931 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE author (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        book_id INTEGER, 
        author_name VARCHAR(128) NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(book_id) REFERENCES book (id)
)


2020-12-11 15:59:26,931 INFO sqlalchemy.engine.base.Engine {}
2020-12-11 15:59:26,937 INFO sqlalchemy.engine.base.Engine COMMIT
'''