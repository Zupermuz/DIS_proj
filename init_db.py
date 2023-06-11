import os
import psycopg2

# Connect to database
conn = psycopg2.connect(
        host="localhost",
        database="dis_db",
        user="postgres",
        password="nielsdata")

# Open cursor for db operations
cur = conn.cursor()

# CREATE SCHEMA
# Open schema.sql file
with open('schema.sql') as f:
     sql_script = f.read()

# Split the script into individual SQL statements
statements = sql_script.split(';')

# Execute each SQL statement
for statement in statements:
    if statement.strip() != '':
        cur.execute(statement)

# FILL DATA POINTS INTO RECIPES
# Open init_recipes.sql file
with open('init_recipes.sql') as f:
    sql_script = f.read()

# Split the script into individual SQL statements
statements = sql_script.split(';')

# Execute each SQL statement
for statement in statements:
    if statement.strip() != '':
        cur.execute(statement)

# FILL DATA POINTS INTO USERS
# Open init_users.sql file
with open('init_users.sql') as f:
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