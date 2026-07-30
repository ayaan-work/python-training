# sqlite3 is Python's built-in module for working with SQLite, a lightweight, file-based relational database. Unlike MySQL or PostgreSQL, SQLite does not require a separate database server—everything is stored in a single file.
import sqlite3

conn = sqlite3.connect("day12/company.db")
cursor=conn.cursor()   #A cursor executes SQL statements.

#whenever we do create, update or delete we have to conn.commit() it. 
cursor.execute(""" CREATE TABLE IF NOT EXISTS employees
                   ( id INTEGER PRIMARY KEY,
                     name TEXT,
                     department TEXT,
                     salary REAL ) """)

conn.commit()

cursor.execute(""" INSERT INTO employees (name, department, salary) VALUES (?, ?, ?) """, ("Alice", "HR", 50000))
conn.commit()

cursor.execute(""" SELECT * FROM employees """)
#The query executes, but nothing is returned until you fetch the results.
# row = cursor.fetchone()  #fetches one result
rows = cursor.fetchall()   #fetches everything
print(rows)

#iterarting over large database
# cursor.execute("SELECT * FROM employees") 
# for row in cursor: 
#     print(row)

# cursor.execute(""" DELETE FROM employees WHERE id IN (2,3,4) """)
# conn.commit()
# rows=cursor.fetchall()
# print(rows)

conn.close()

