import pymysql

# 创建mysql连接
db = pymysql.connect('node1', 'devops', 'qwe123456', 'db1')

try:
    # 使用cursor()方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        # 拼接SQL
        sql = '''SELECT VERSION()'''
        # 使用execute()方法 执行SQL
        cursor.execute(sql)
        # 获取执行结果
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f'fetch error {e}')
finally:
    db.close()

print(f'Database version: {result}')



'''
out:
Database version: ('5.7.32',)
'''