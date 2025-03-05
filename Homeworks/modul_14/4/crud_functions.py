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
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Products (price)')
    # Первичное заполнение базы
    # for i in range(1, 5):
    #     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                    (f'Название: {i}', f'Описание: {i} {str(random.randint(1000, 5000))}',
    #                     (random.randint(100, 500)) * i))


def get_all_products():
    cursor.execute('SELECT id, title, description, price FROM Products')
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products

# initiate_db()
