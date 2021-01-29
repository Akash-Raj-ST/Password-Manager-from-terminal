
import sqlite3

conn = sqlite3.connect("password_db.db")
cursor = conn.cursor()

sql_comm = '''CREATE TABLE IF NOT EXISTS INFO(No INTEGER PRIMARY KEY,
                                Website VARCHAR,
                                username VARCHAR,
                                Gmail VARCHAR,
                                Password VARCHAR,
                                info VARCHAR)'''

cursor.execute(sql_comm)

