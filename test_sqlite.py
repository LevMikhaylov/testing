import sqlite3
import pytest

@pytest.fixture
def db_connection():
    # Подключение к базе данных
    conn = sqlite3.connect(':memory:')  # Создаем временную базу данных в памяти
    cursor = conn.cursor()
    
    # Настройка базы данных (создание таблиц и т.д.)
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
    
    yield conn  # Возвращаем соединение для использования в тестах

    conn.close()  # Закрываем соединение после тестов

def test_db_insert_and_fetch(db_connection):
    cursor = db_connection.cursor()
    
    # Добавление данных
    cursor.execute("INSERT INTO users (name) VALUES ('Тест пользователь')")
    db_connection.commit()
    
    # Получение данных
    cursor.execute("SELECT name FROM users WHERE id=1")
    result = cursor.fetchone()
    
    assert result[0] == 'Тест пользователь', "Имя пользователя не совпадает с ожидаемым"
