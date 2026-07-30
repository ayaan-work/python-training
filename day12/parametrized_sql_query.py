# When interacting with a database, never insert user input directly into an SQL query. Instead, use parameterized queries, where the SQL statement and the data are sent to the database separately. This prevents SQL injection, improves code readability, and allows the database to handle data types correctly.

import sqlite3
conn = sqlite3.connect("day12/company1.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS employees
                   ( id INTEGER PRIMARY KEY,
                     name TEXT,
                     department TEXT,
                     salary REAL ) """)
conn.commit()

#dictionary style parameterized query
cursor.execute(""" INSERT INTO employees (name, department, salary) VALUES (:name,:department,:salary) """, 
            {
                "name":"Ayaan",
                "department":"IT",
                "salary":"60000"}
        )
conn.commit()

cursor.execute( """ SELECT * 
                FROM employees
                WHERE department = :dept """, {"dept": "IT"} ) 

rows = cursor.fetchall() 
print(rows)
conn.close()