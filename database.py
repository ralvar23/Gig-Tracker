import sqlite3

def get_db():
    conn = sqlite3.Connection("gig_tracker.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

with open("schema.sql") as f:
    conn.executescript(f.read())

conn.close()
print("Database created")
