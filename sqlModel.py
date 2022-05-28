import pymysql
from config import *

def Connect_db():
    try:
        connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
        )
        print('successfully connected...')
        print('#' * 20)

        try:
            with connection.cursor() as cursor:
                create_table_query = 'INSERT INTO `classmates`(`first_name`, `last_name`, `group_num`, `prioruty`) ' \
                                     'VALUES ()'
        finally:
            connection.close()
    except Exception as ex:
        print('connection refused...')
        print(ex)

