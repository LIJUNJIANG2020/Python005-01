# Python与MySQL相关模块

## 概念

其它语言： 连接器、绑定、binding

Python语言： Python Database API、DB-API

## 模块

- MySQLdb

    >  Python2的包，适用于MySQL5.5和Python 2.7

- mysqlclient

    > Python3中安装的MySQLdb 包叫做mysqlclient, 加载的依然是MySQLdb
    >
    > 安装： pip install mysqlclient  
    >
    > 导入： import MySQLdb

- 其它DB-API:

    - pymysql       # 流行度最高

        > pip install pymysql

    - mysql-connector-python     # MySQL 官方

        > pip install mysql-connector-python 

- 使用ORM (对象映射关系)

    - sqlalchemy

        > pip install sqlalchemy

---

# PyMySQL

> 流行度最高
>
> 一般使用步骤
>
> 1. 导入pymysql模块
> 2. 建立数据库连接、获取游标
> 3. 拼接SQL
> 4. 执行SQL
> 5. 关闭游标、mysql 连接

## pymysql 连接mysql 

> [完整示例](./示例/pymysql_connect.py)

```python
# 安装 pymysql 模块
In [1]: pip install pymysql                                                                                                     
Requirement already satisfied: pymysql in ./anaconda3/lib/python3.8/site-packages (0.10.1)
Note: you may need to restart the kernel to use updated packages.

# 导入pymysql 模块
In [2]: import pymysql                                                                                                          

# 创建连接
In [3]: db = pymysql.connect('localhost', 'devops', 'qwe123456', 'db1')                                                         

In [4]: print(db)                                                                                                               
<pymysql.connections.Connection object at 0x7f4f714b2cd0>

```

- 游标操作

```python
In [5]: with db.cursor() as cursor: 
...:     sql = '''SELECT VERSION()''' 
...:     cursor.execute(sql) 
...:     result = cursor.fetchone() 
...:                                                                                                                         

In [6]: db.commit()                                                                                                             

In [7]: db.close()                                                                                                              

In [8]: print(result)                                                                                                           
('5.7.32',)

```

   

## pymysql操作数据库

> 插入

```python
# insert 操作 插入单行记录
import pymysql

db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')

try:
    with db.cursor() as cursor:
        # %s 在pymsql中是固定的占位符，数字、字符串通用
        sql = '''insert into book (id, name) values (%s, %s)'''
        value = (1002, '圣墟')
        cursor.execute(sql, value)   # execute() 方法

    db.commit()

except Exception as e:
    print(f'insert error {e}')
finally:
    db.close()
    print(cursor.rowcount)
    
'''Out
1
'''
############################################
# 批量插入多行记录
import pymysql

db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')

try:
    with db.cursor() as cursor:
        sql = '''insert into book (id, name) values (%s, %s)'''
        values = (
            (1004, '遮天'),
            (1005, '完美世界')
        ) 
        cursor.executemany(sql, values)  # executemany() 方法
    db.commit()

except Exception as e:
    print(f'insert many error {e}')

finally:
    db.close()
    print(cursor.rowcount)

'''Out
2

#########
mysql> select * from book;
+------+--------------+
| id   | name         |
+------+--------------+
| 1004 | 遮天         |
| 1005 | 完美世界     |
+------+--------------+
2 rows in set (0.00 sec)

'''


```

> 查询

```python
import pymysql

db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')

try:
    with db.cursor() as cursor:
        sql = 'select name from book'
        cursor.execute(sql)
        book = cursor.fetchone()   # fetchone()  取第一条查询结果

        cursor.execute(sql)        # 
        books = cursor.fetchall()  # fetchall()  取所有查询结果
        print(f'book: {book}')
        print(f'books: {books}')
    db.commit()

except Exception as e:
    print(f'select error: {e}')

finally:
    db.close()
    print(cursor.rowcount)
    
'''Out
book: ('圣墟',)
books: (('圣墟',),)
1
'''

```

> 更新

```python
import pymysql

db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')

try:
    with db.cursor() as cursor:
        sql = 'update book set name = %s where id = %s'
        value = ('神墓', 1002)
        cursor.execute(sql, value)
    db.commit()
except Exception as e:
    print(f'update error {e}')

finally:
    db.close()
    print(cursor.rowcount)

'''Out
1
mysql> select * from book;
+------+--------+
| id   | name   |
+------+--------+
| 1002 | 神墓   |
+------+--------+
1 row in set (0.00 sec)

'''

```

> 删除

```python
import pymysql

db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')

try:
    with db.cursor() as cursor:
        sql = 'delete from book where name = %s'
        value = ("神墓")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f'delete errer {e}')
finally:
    db.close()
    print(cursor.rowcount)

'''Out
1
####
mysql> select * from book;
Empty set (0.01 sec)
'''
```

## pymysql 配置文件

> 抽离mysql的连接信息，防止硬编码，便于管理和复用

```ini
[mysql]
host = 'node1'
user = 'devops'
password = 'qwe123456'
database = 'testdb1'
port = 3306
```

> 获取配置文件内容

~~~python
from configparser import ConfigParser

def get_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return dict(items)

if __name__ == '__main__':
    print(get_db_config())
~~~

> 使用

```python
import pymysql
from get_db_config import get_db_config


# db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')
info = get_db_config()
db = pymysql.connect(**info)
```



