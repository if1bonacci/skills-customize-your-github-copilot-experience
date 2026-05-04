# SQLite Databases Starter Code

"""
This starter code provides a basic structure for working with SQLite in Python.
Complete the tasks in the assignment README to build out the full solution.
"""

import sqlite3

DB_NAME = 'resources.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Create table (customize columns as needed)
    c.execute('''
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add CRUD operation functions below

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
