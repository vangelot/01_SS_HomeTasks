import mysql.connector
from dotenv import load_dotenv
import os
import sql_queries


def main():
    load_dotenv()

    password = os.getenv('LOCAL_DB_PASSWORD')

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password,
        autocommit=True
    )

    my_cursor = mydb.cursor()

    sql = sql_queries.insert1
    val = (1, 'John')

    my_cursor.execute(sql, val)
    # res = my_cursor.fetchall()
    mydb.commit()

    sql = sql_queries.insert2
    val = (1, 'John', 10000)
    #
    # my_cursor.execute(sql, val)

    # my_cursor.execute(sql_queries.insert)


if __name__ == '__main__':
    main()