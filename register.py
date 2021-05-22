import bcrypt
import sqlite3
from sqlite3 import Error


def main():
    register_email = input("What is your email address: ")
    register_username = input("Choose a username: ")
    register_password = input("Choose a password: ")

    register_salt = bcrypt.gensalt()

    register_password_hashed = bcrypt.hashpw(
        register_password.encode('utf-8'), register_salt)

    register_email_hashed = bcrypt.hashpw(
        register_email.encode('utf-8'), register_salt)

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS members(username TEXT PRIMARY KEY, email TEXT, password TEXT, salt TEXT)
            """
    cursor.execute(command1)
    command2 = ("INSERT INTO members VALUES('" + register_username + "', '" +
                register_email_hashed.decode('ascii') + "', '" + register_password_hashed.decode('ascii') +
                "', '" + register_salt.decode('ascii') + "')")
    cursor.execute(command2)
    members_list = cursor.execute("SELECT * FROM 'members'")
    print(members_list.fetchall())
    conn.commit()
    cursor.close()
    conn.close()


main()
