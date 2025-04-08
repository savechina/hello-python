import sqlite3

# Connect to SQLite database (creates a new file if it doesn't exist)
# conn = sqlite3.connect("data/example.db")
conn = sqlite3.connect(":memory:")  # connect to a database in RAM

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
"""
)

# Insert some sample data
cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
    ("John Doe", "IT", 75000.00),
)
cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
    ("Jane Smith", "HR", 65000.00),
)
cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
    ("Bob Johnson", "Finance", 80000.00),
)

# Commit the changes
conn.commit()

# Query the data
print("All employees:")
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: {row[3]}")

# Query with condition
print("\nEmployees with salary > 70000:")
cursor.execute("SELECT name, salary FROM employees WHERE salary > ?", (70000,))
for row in cursor.fetchall():
    print(f"Name: {row[0]}, Salary: {row[1]}")

# Update data
cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (85000.00, "John Doe"))
conn.commit()

# Delete data
cursor.execute("DELETE FROM employees WHERE name = ?", ("Jane Smith",))
conn.commit()

# Show final state
print("\nFinal employee list:")
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: {row[3]}")

# Close the connection
conn.close()
