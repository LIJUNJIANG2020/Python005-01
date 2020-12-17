import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
from sqlalchemy_insert_select import Book_table, Auther_talbe

dburl = 'mysql+pymysql://devops:qwe123456@node1:3306/testdb1?charset=utf8mb4'
engine = create_engine(dburl, echo=True, encoding='utf-8')

SessionClass = sessionmaker()
session = SessionClass(bind=engine)

# # 更新
result = session.query(Book_table)
result = result.filter(Book_table.book_id == 7)
result.update({Book_table.book_name : '圣墟'})
session.commit()

'''Out
mysql> select * from bookorm;
+---------+--------------+
| book_id | book_name    |
+---------+--------------+
|       7 | 完美世界     |
|       8 | 摭天         |
|       9 | 神墓         |
+---------+--------------+
3 rows in set (0.00 sec)

mysql> select * from bookorm;
+---------+-----------+
| book_id | book_name |
+---------+-----------+
|       7 | 圣墟      |
|       8 | 摭天      |
|       9 | 神墓      |
+---------+-----------+
3 rows in set (0.00 sec)

'''

# # 删除
## 删除一个
# result = session.query(Book_table)
# result = result.filter(Book_table.book_id == 7)
# session.delete(result.one())
# session.commit()

'''Out
mysql> select * from bookorm;
+---------+-----------+
| book_id | book_name |
+---------+-----------+
|       7 | 圣墟      |
|       8 | 摭天      |
|       9 | 神墓      |
+---------+-----------+
3 rows in set (0.00 sec)

mysql> select * from bookorm;
+---------+-----------+
| book_id | book_name |
+---------+-----------+
|       8 | 摭天      |
|       9 | 神墓      |
+---------+-----------+
2 rows in set (0.00 sec)


'''
# 删除查询出的所有
# result = session.query(Book_table)
# result = result.filter(Book_table.book_id == 8)
# result.delete()
# session.commit()
'''
result = session.query(Book_table)
result = result.filter(Book_table.book_id == 7)
session.delete(result.one())
session.commit()
'''