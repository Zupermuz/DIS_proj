import psycopg2
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.exceptions import abort

app = Flask(__name__)

app.config[ 'SECRET KEY' ] = 'uU6lD70kLc5E49t5B0gRy32jA8P4iQ6Y9m5N4v7J2x1l3b4G1'

# Set your own database 
# Ex. db = "dbname='dis_db' user = 'user' host = '127.0.0.1' password = 'dis'"
db = "dbname='dis_db' user = 'postgres' host = '127.0.0.1' password = 'nielsdata'"
#conn = psycopg2.connect(db)
def get_db_connection():
    conn = psycopg2.connect(db)
    return conn

# bcrypt = Bcrypt(app)

# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

from routes import RoutesBlueprint
app.register_blueprint(RoutesBlueprint)


if __name__ == '__main__':
    app.run(debug=True)