# SQLAlchemy

> 将sql操作抽象成三层
>
> 业务逻辑
>
> 持久层
>
> 数据库层
>
> 优点：可以通过持久层实现业务的逻辑关系，而不必考虑数据库层是如何实现
>
> 缺点：持久层转化为sql会造成性成损耗，ORM抽象出的功能不覆盖所有sql, 不易于实现复杂的sql操作

## 连接MySQL

```python
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData

# echo=True  开启调试 
engine = create_engine('mysql+pymysql://devops:qwe123456@node1:3306/db1', echo=True)
# print(engine) # Out: Engine(mysql+pymysql://devops:***@node1:3306/db1)
```

##  两种模式

### SQLAlchemy core 方式

```python
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
```

### SQLAlchemy ORM 方式

```python
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
```

## 操作

> 插入数据

```

```

> 查询数据

```

```

> 更新数据

```

```

> 删除数据

~~~

~~~

