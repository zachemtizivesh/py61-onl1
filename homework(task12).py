#Вы разрабатываете систему для управления библиотекой.
#Необходимо создать базу данных книг, читателей и выдачи книг с помощью SQLite3 и Python-классов.
#1.	Создайте базу данных library.db, содержащую 3 таблицы:

import sqlite3
# Создаем соединение с базой данных (или создаем ее, если она не существует)
conn = sqlite3.connect('library.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL,
    status TEXT CHECK(status IN ('available', 'borrowed')) NOT NULL
)
''')

# Создаем таблицу readers
cursor.execute('''
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Создаем таблицу borrowed_books
cursor.execute('''
CREATE TABLE IF NOT EXISTS borrowed_books (
    reader_id INTEGER,
    book_id INTEGER,
    borrow_date TEXT NOT NULL,
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    PRIMARY KEY (reader_id, book_id)
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных и таблицы успешно созданы.")


#2.	Используйте dataclass для представления книг и читателей.

from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str  # 'available' or 'borrowed'

@dataclass
class Reader:
    id: int
    name: str
    age: int
    borrowed_books: Optional[list[int]] = None  # Список ID книг, которые взяты на время

# Пример использования
if __name__ == "__main__":
    book1 = Book(id=1, title="1984", author="George Orwell", year=1949, status="available")
    reader1 = Reader(id=1, name="Alice", age=30, borrowed_books=[1])

    print(book1)
    print(reader1)