import os
import psycopg2

# Connect to database
conn = psycopg2.connect(
        host="localhost",
        database="dis_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open cursor for db operations
cur = conn.cursor()

# Open schema.sql file
with open('schema.sql') as f:
     sql_script = f.read()

# Split the script into individual SQL statements
statements = sql_script.split(';')

# Execute each SQL statement
for statement in statements:
    if statement.strip() != '':
        cur.execute(statement)

# Commit and close cursor and connection
conn.commit()

cur.close()
conn.close()