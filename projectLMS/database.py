import sqlite3

connection=sqlite3.connect("library.db")
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT NOT NULL,
category TEXT NOT NULL,
copies INTEGER NOT NULL CHECK(copies >= 0)

)
""")

cursor.execute("""
CREATE TABLE IF  NOT EXISTS members(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
phone TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS loans(
id INTEGER PRIMARY KEY,
book_id INTEGER NOT NULL,
member_id INTEGER NOT NULL,
borrow_date TEXT NOT NULL DEFAULT CURRENT_DATE,
return_date TEXT ,
FOREIGN KEY(book_id) REFERENCES books(id),
FOREIGN KEY(member_id) REFERENCES members(id)
)
""")

connection.commit()
