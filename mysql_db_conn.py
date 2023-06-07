#pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password="root",
    database="c361_pm"
)

cursor=connection.cursor()

create_table_query = """CREATE TABLE table_name1(
    id int auto_increment primary key,
    column1 varchar(250),
    column2 varchar(250)
    )"""
    
cursor.execute(create_table_query)
print("table created successfully")

insert_query = "INSERT INTO table_name1 (column1,column2) values(%s,%s)"
data=("value1",87)
cursor.execute(insert_query,data)
connection.commit()

select_query="select * from table_name1"
cursor.execute(select_query)
rows=cursor.fetchall()
for i in rows:
    print(i)
    
drop_query="drop table table_name1"
cursor.execute(drop_query)