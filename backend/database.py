import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "leads.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def create_lead(name: str, phone: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO leads (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    conn.commit()
    conn.close()
