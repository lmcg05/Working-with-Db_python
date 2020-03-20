import mysql.connector as mysql

mydb = mysql.connect(
  host="34.76.141.152",
  user="root",
  passwd="Pinkwine123",
  database="my_database1"
)

mycursor = mydb.cursor()
#creating a Databse
#mycursor.execute("CREATE DATABASE my_database")

#creating a table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#inserting a row
#sql = "INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')"
#mycursor.execute(sql)

#sql = "INSERT INTO customers (name, address) VALUES ('Ash', 'Highway 22')"
#mycursor.execute(sql)

#SELECT FROM TABLE
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for customer in myresult:
  print(customer)

mydb.commit()

print(mycursor.rowcount, "record inserted.")