import sqlite3
from sqlite3 import Error


def main():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")

    print(cursor.fetchall())


main()
