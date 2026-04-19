import os
import subprocess
import hashlib
import random
import sqlite3
import pickle

API_KEY = "12345-SECRET-KEY"
PASSWORD = "admin123"


def weak_password_hash(password):
    return hashlib.md5(password.encode()).hexdigest()


def run_user_command(user_input):
    os.system("echo " + user_input)


def run_subprocess(user_input):
    subprocess.Popen("dir " + user_input, shell=True)


def unsafe_sql(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    results = cursor.fetchall()
    conn.close()
    return results


def insecure_random():
    return random.randint(1000, 9999)


def unsafe_deserialization(data):
    return pickle.loads(data)


def login():
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == "admin" and pwd == PASSWORD:
        print("Login successful")
    else:
        print("Invalid login")


if __name__ == "__main__":
    print("Weak hash:", weak_password_hash("mypassword"))
    print("Security code:", insecure_random())
    login()