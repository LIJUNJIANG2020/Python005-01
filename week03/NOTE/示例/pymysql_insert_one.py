import pymysql
from get_db_config import get_db_config


# db = pymysql.connect('node1', 'devops', 'qwe123456', 'testdb1')
info = get_db_config()
db = pymysql.connect(**info)

try:
    with db.cursor() as cursor:
        # %s 在pymsql中是固定的占位符，数字、字符串通用
        sql = '''insert into book (id, name) values (%s, %s)'''
        value = (1002, '圣墟')
        cursor.execute(sql, value)

    db.commit()

except Exception as e:
    print(f'insert error {e}')
finally:
    db.close()
    print(cursor.rowcount)