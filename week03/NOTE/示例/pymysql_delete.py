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