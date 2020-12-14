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

