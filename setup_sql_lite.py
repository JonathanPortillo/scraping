import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('indeed.db')
cursor = conn.cursor()

# Create a new table
cursor.execute('''
CREATE TABLE IF NOT EXISTS job_listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    location TEXT NOT NULL,
    job_description TEXT NOT NULL,
    salary TEXT NOT NULL
);
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")