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