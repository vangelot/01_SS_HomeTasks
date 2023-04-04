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
        password=password
    )

    print(mydb)

    my_cursor = mydb.cursor()
    my_cursor.execute(sql_queries.create_database)

    # my_cursor.execute("DROP DATABASE IF EXISTS my_first_db1")
    # my_cursor.execute("SHOW DATABASES")

    # my_cursor.execute(sql_queries.drop_student)

    # my_cursor.execute(sql_queries.create_table_student)
    # results = my_cursor.fetchall()

    my_cursor.execute(sql_queries.create_table_employee)

    mydb.commit()
    # my_cursor.close()

    # print(my_cursor)


if __name__ == '__main__':
    main()