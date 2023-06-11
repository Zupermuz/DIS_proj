from website import app, set_db
from website.init_db import set_and_init_db

# Set your own database 
# Ex. db = "dbname='dis_db' user = 'user' host = '127.0.0.1' password = 'dis'"
db = "dbname='dis_db' user = 'postgres' host = '127.0.0.1' password = 'dis'"

# init database
set_and_init_db(db) # uncomment this for first run
set_db(db)

if __name__ == '__main__':
    app.run(debug=True)