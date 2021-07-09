import sqlite3

conn = sqlite3.connect("database.db")

print("opened database successfully")

conn.execute("CREATE TABLE students(roll_no TEXT,name TEXT,fname TEXT,phone TEXT,cinic TEXT,program TEXT,session TEXT,fees TEXT)")

print("table created successfully")

conn.close()