import sqlite3

def new_table(name_db: str, name_table:str):
    conn = sqlite3.connect(f"{name_db}")
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {name_table} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        price INTEGER
    )
        """)

    conn.commit()
    conn.close()

def insert_object(db_name: str, name_table: str, level_id: int, price: int): #Добавление элементов в бд
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(
        f'INSERT INTO {name_table} (id, price) VALUES (?, ?)', 
        (level_id, price)
    )
    connection.commit()
    connection.close()


def count_levels(db_name: str, table_name: str) -> int: #Подчет элементов в бд
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    count = cursor.fetchone()[0]
    connection.close()
    return count


def take_object(db_name: str, table_name: str, index_object: int): #Взять элемент
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT id FROM {table_name}
        ORDER BY id
        LIMIT 1 OFFSET ?;
    """, (index_object,))
    row = cursor.fetchone()
    connection.close()
    return row[0] if row else None

