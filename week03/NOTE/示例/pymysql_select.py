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