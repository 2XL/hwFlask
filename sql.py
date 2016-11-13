import sqlite3

"""
test it by
python db.py
"""
with sqlite3.connect(database="sample.db") as connection:
    cursor = connection.cursor()
    try:
        cursor.execute("""DROP TABLE IF EXISTS posts""")
    except sqlite3.OperationalError:
        pass
    cursor.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
    cursor.execute('INSERT INTO posts VALUES("Good", "Good person")')
    cursor.execute('INSERT INTO posts VALUES("Bad", "Bad person")')
