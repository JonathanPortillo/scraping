import sqlite3
import csv

# Filepath to the CSV file
csv_file_path = "sample_data.csv"

# Connect to the SQLite database
conn = sqlite3.connect("indeed.db")
cursor = conn.cursor()

# Open the CSV file and read its contents
with open(csv_file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Use DictReader to map column names to values
    for row in reader:
        # Insert data into the job_listings table
        print(row)
        cursor.execute('''
            INSERT INTO job_listings (company, location, job_description, salary)
            VALUES (?, ?, ?, ?)
        ''', (row["company"], row["location"], row["job_description"], row["salary"]))

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Data successfully inserted into the database.")