from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = '98as89d7a078s9dg6a908sd7f6a8s7d9f6as67df'


# Set your own database 
# Ex. db = "dbname='dis_db' user = 'user' host = '127.0.0.1' password = 'dis'"
db = db = "dbname='dis_db' user = 'postgres' host = '127.0.0.1' password = 'dis'"
conn = psycopg2.connect(db)

# Open cursor for db operations
cur = conn.cursor()

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'



from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
