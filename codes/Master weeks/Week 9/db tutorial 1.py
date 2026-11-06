# A database is an organized collection of data or information stored electronically in a computer system.
# Unlike a simple file or spreadsheet, a database is managed by software known as a 
# Database Management System (DBMS). 
# The DBMS allows multiple users and applications to safely store, update, search, and retrieve 
# large amounts of data quickly and securely.

# Types of Database:
# 1. Relational    ---->  Store data in structured tables with rows and columns (like a grid). 
#                         They use a language called SQL (Structured Query Language) to query and 
#                         manage data. Examples include MySQL, PostgreSQL, and Oracle.

# 2. Non-Relational/NOSQL ---->  Designed to store unstructured or semi-structured data—such as 
#                                 videos, documents, social media posts, or IoT sensor logs—using formats 
#                                 like key-value pairs, graphs, or documents. 
#                                 Examples include MongoDB and Redis

import sqlite3

conn = sqlite3.connect("test.db")
print("Database openned successfully...")

c = conn.cursor()

# ------------------------------------------
# 1. Create db table
# ------------------------------------------
# query = """CREATE TABLE students(
# FIRST text,
# LAST text,
# age INT,
# EMAIL text,
# ID VARCHAR
# )"""
# c.execute(query)

# ------------------------------------------
# 2. INSERT into db table
# ------------------------------------------
c.execute("INSERT INTO students (FIRST, LAST, age, EMAIL, ID) \
          VALUES ('Raja', 'Ahsan', 30, 'xyz@gmail.com', 1)")
c.execute("INSERT INTO students (FIRST, LAST, age, EMAIL, ID) \
          VALUES ('Raja', 'Ehsan', 30, 'xyz@gmail.com', 1)")
c.execute("INSERT INTO students (FIRST, LAST, age, EMAIL, ID) \
          VALUES ('Raja', 'Saad', 30, 'xyz@gmail.com', 1)")
conn.commit()

# ------------------------------------------
# 3. fetch data db table
# ------------------------------------------

# ---------------------
# a. fetch all data
# --------------------
cursor = c.execute("SELECT * from students")
for row in cursor:
    print(f"First: {row[0]}")
    print(f"Last: {row[1]}")
    print(f"Age: {row[2]}")
    print(f"Email: {row[3]}")
    print(f"ID: {row[4]}")

# ---------------------
# b. fetch specific data
# --------------------
# cursor = c.execute("SELECT * from students WHERE LAST='Saad' AND age=31")
# for row in cursor:
#     print(f"First: {row[0]}")
#     print(f"Last: {row[1]}")
#     print(f"Age: {row[2]}")
#     print(f"Email: {row[3]}")
#     print(f"ID: {row[4]}")

# ------------------------------------------
# 4. Update data db table
# ------------------------------------------
# c.execute("UPDATE students SET FIRST='Ubaid', LAST='MEMON' WHERE LAST='Saad'")

# ------------------------------------------
# 5. Delete record from db table
# ------------------------------------------
# c.execute("DELETE from students WHERE ID=1")

# conn.commit()
# print("created table successfully")
conn.close()