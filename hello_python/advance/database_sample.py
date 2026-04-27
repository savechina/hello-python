"""
Database Sample (PyMySQL).
Demonstrates MySQL database connection and basic operations.
Note: Requires a running MySQL server. See database_sqlite_sample.py for a self-contained alternative.
"""

import pymysql

# Database configuration (replace with your actual credentials)
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "your_password",
    "database": "test_db",
}


def connect_sample():
    """Demonstrates MySQL connection with error handling."""
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print(f"Database version: {data}")
        cursor.close()
        db.close()
    except pymysql.Error as e:
        print(f"MySQL connection failed (expected without a running server): {e}")
        print("Hint: Use database_sqlite_sample.py for a self-contained demo with no server required.")


def query_sample():
    """Demonstrates basic SQL operations (placeholder, requires live DB)."""
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS demo (id INT PRIMARY KEY, name VARCHAR(50))")
        cursor.execute("INSERT INTO demo (id, name) VALUES (1, 'Python')")
        db.commit()
        cursor.execute("SELECT * FROM demo")
        rows = cursor.fetchall()
        for row in rows:
            print(f"  row: {row}")
        cursor.execute("DROP TABLE demo")
        db.commit()
        cursor.close()
        db.close()
    except pymysql.Error as e:
        print(f"Query failed (expected without a running server): {e}")


if __name__ == "__main__":
    connect_sample()
    print("---")
    query_sample()
