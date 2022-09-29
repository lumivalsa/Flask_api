# Import required modules
import csv
import sqlite3
  
# Connecting to the geeks database
connection = sqlite3.connect('/Users/luismi/Documents/Proyectos/Ejercicio_flask/Flask_api/data/datos.db')
  
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()
  
# Table Definition
create_table = '''CREATE TABLE datos(
                TV integer,
                radio integer,
                newspaper integer,
                sales integer);
                '''
  
# Creating the table into our 
# database
cursor.execute(create_table)
  
# Opening the person-records.csv file
file = open('/Users/luismi/Documents/Proyectos/Ejercicio_flask/Flask_api/data/Advertising.csv')
  
# Reading the contents of the 
# person-records.csv file
contents = csv.reader(file)
  
# SQL query to insert data into the
# person table
insert_records = "INSERT INTO datos (TV, radio,newspaper,sales) VALUES(?,?,?,?)"
  
# Importing the contents of the file 
# into our person table
cursor.executemany(insert_records, contents)
  
# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully 
# inserted into the table
select_all = "SELECT * FROM datos"
rows = cursor.execute(select_all).fetchall()
  
# Output to the console screen
for r in rows:
    print(r)
  
# Commiting the changes
connection.commit()
  
# closing the database connection
connection.close()