import psycopg2
from config import params

def connect():
    # Просто подключаемся, используя данные из config.py
    conn = psycopg2.connect(**params)
    print("Связь с базой установлена!")
    return conn

if __name__ == '__main__':
    # Проверяем, работает ли функция
    my_connection = connect()
    my_connection.close()
    print("Связь закрыта.")