create_database = '''
CREATE DATABASE IF NOT EXISTS my_first_db
'''

create_table_student = '''
USE my_first_db;
CREATE TABLE IF NOT EXISTS student (
    id INT,
    name VARCHAR(255)
) ;
'''

drop_student = '''
USE my_first_db;
DROP TABLE IF EXISTS student
'''

create_table_employee = '''
USE my_first_db;
CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    salary INT(6)
) ;
'''

alter_table_student = '''
USE my_first_db;
ALTER TABLE student
MODIFY id INT NOT NULL PRIMARY KEY;
'''

insert1 = '''
USE my_first_db;
INSERT INTO student (id, name) VALUES (%s, %s)
'''

insert2 = '''
USE my_first_db;
INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)
'''

insert = '''
USE my_first_db;
INSERT INTO student (id, name) VALUES (50, 'John');
INSERT INTO employee (id, name, salary) VALUES (50, 'John', 10000);
'''