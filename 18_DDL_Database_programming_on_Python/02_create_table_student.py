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

    my_cursor = mydb.cursor()

    my_cursor.execute(sql_queries.create_table_student)


if __name__ == '__main__':
    main()