import bcrypt
import sqlite3
from sqlite3 import Error


def main():
    login_username = input("What is your username: ")
    login_password = input("What is your password: ")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members WHERE username = '" +
                   login_username + "'")

    user = cursor.fetchall()
    try:
        user = user[0]

        salt = user[3]
        password = user[2]

        hashed = bcrypt.hashpw(login_password.encode(
            'utf-8'), salt.encode('utf-8'))
        hashed = hashed.decode('utf-8')

        if password == hashed:
            print("Login successful!")
        else:
            print("Wrong password")
    except:
        print("Account does not exist")


main()
