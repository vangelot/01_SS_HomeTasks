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

    """
        This also works:
        two command in 1 query:
        
    my_cursor.execute(sql_queries.insert)
    """

    sql = sql_queries.insert1
    val = (1, 'John')

    my_cursor.execute(sql, val)
    results = my_cursor.fetchall()

    # my_cursor.close()

    if not mydb.is_connected():
        # reconnect the cursor
        mydb.reconnect(attempts=3, delay=0)

    # my_cursor = mydb.cursor()
    # sql = sql_queries.insert1
    # val = (37, 'John')

    # my_cursor.execute(sql, val)
    # results2 = my_cursor.fetchall()


    # res = my_cursor.fetchall()
    # mydb.commit()

    sql = sql_queries.insert2
    val = (1, 'John', 10000)
    #
    my_cursor.execute(sql, val)

    my_cursor.close()
    mydb.close()
    # my_cursor.execute(sql_queries.insert)


if __name__ == '__main__':
    main()
