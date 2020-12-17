import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# 创建表
class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(book_id='{self.book_id}', " \
            "book_name={self.book_name})".format(self=self)


class Auther_talbe(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 实例化一个引擎
dburl = 'mysql+pymysql://devops:qwe123456@node1:3306/testdb1?charset=utf8mb4'
engine = create_engine(dburl, echo=True, encoding='utf-8')

# 创建数据库
Base.metadata.create_all(engine)

# 创建 session, 建立会话，默认会打开一个事务
SessionClass = sessionmaker(bind=engine)
session = SessionClass()


# 增加数据
book_demo = Book_table(book_name='完美世界')
book_demo2 = Book_table(book_name='摭天')
book_demo3 = Book_table(book_name='神墓')

auther_demo = Auther_talbe(username='辰东')

# 查看数据
# print(book_demo)
# print(auther_demo)

# 插入数据
# session.add(book_demo)
# session.add(book_demo2)
# session.add(book_demo3)
# session.add(auther_demo)

# # 提交，事务结束
# session.commit()
# # 不会commit 也不会结束事务
# session.flush()


####  查询操作
# # 查询所有book
# results = session.query(Book_table).all()
# print(results)

# # 迭代代替all
# for result in session.query(Book_table):
#     print(result)

# # frist() 查询第一条
# result = session.query(Book_table).first()

# # one()   查询一条信息，结果多条时会抛出导异常
# try:
#     result = session.query(Book_table).one()
#     
# except Exception as e:
#     print(f'query error: {e}')
'''Out
query error: Multiple rows were found for one()
'''

# # scalar() 返回第一个结果的第一个元素，没结果返回None , 多于一个结果也会抛异常
# try:
#     result = session.query(Book_table).scalar()
    
# except Exception as e:
#     print(f'query error: {e}')


# # 查询指定的列
# result = session.query(Book_table.book_name).first()

# ##  排序 
# # 正向
# for result in session.query(Book_table.book_name).order_by(Book_table.book_id):
#     print(result)
# # 反向
# from sqlalchemy import desc
# for result in session.query(Book_table.book_name).order_by(desc(Book_table.book_id)):
#     print(result)


# # 限制返回条数
# results = session.query(Book_table.book_name).order_by(Book_table.book_id).limit(2)
# print([result.book_name for result in results])


# # 使用聚合函数
# from sqlalchemy import func
# print(session.query(func.count(Book_table.book_name)).first())

# # 过滤
# print(session.query(Book_table).filter(Book_table.book_id > 8 ).all())
# print(session.query(Book_table).filter(Book_table.book_id > 7, Book_table.book_id < 9).all())
# 与 或 非
# from sqlalchemy import add_, or_, not_
# print(session.query(Book_table).filter(or_(
#                                         Book_table.book_id > 7,
#                                         Book_table.book_id < 9)).all())


session.commit()