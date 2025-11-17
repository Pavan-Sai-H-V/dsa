import pymysql
from password_masking.password_utils import get_decrypt_password
connection=pymysql.connect(
    host="localhost",
    user='root',
    password=get_decrypt_password(),
    database='test',
    cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        create_query="""
         CREATE TABLE IF NOT EXISTS employees(
          id INT AUTO_INCREMENT PRIMARY KEY, 
          name VARCHAR(50),
          department VARCHAR(30));
          """
        cursor.execute(create_query)

        insert_query="INSERT INTO employees(name,department) VALUES(%s,%s)"
        values=[('John','IT'),('Joe','CSE'),('Berry','BCA'),('Salsa','EEE')]
        cursor.executemany(insert_query,values)
        connection.commit()

        select_query="SELECT * FROM employees"
        cursor.execute(select_query)
        result=cursor.fetchall()

        with open('emp_out.txt','w') as f:
            for r in result:
             f.write(f"{r}\n")

finally:
    connection.close()