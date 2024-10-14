import random
import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_product ON Products (title)')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_user ON Users (username)')
    connection.commit()
    # #### Первичное заполнение базы
    # for i in range(1, 5):
    #     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                    (f'Название: {i}', f'Описание: {i} {str(random.randint(1000, 5000))}',
    #                     (random.randint(100, 500)) * i))


def get_all_products():
    cursor.execute('SELECT id, title, description, price FROM Products')
    all_products = cursor.fetchall()
    connection.commit()
    return all_products


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    result = False
    all_user = cursor.execute('SELECT username FROM Users').fetchall()
    for i in all_user:
        if i[0] == username:
            result = True
            break
    connection.commit()
    return result

# initiate_db()
# connection.commit()
# connection.close()
