from . import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


@login_manager.user_loader
def load_user(user_id):
    user_data = getUserDataById(user_id)
    if user_data:
        return User(user_data['username'], user_data['password'], user_data['ingr_list'])
    return None
    
    
    


class User(tuple, UserMixin):
    def __init__(self, usr_data):
        self.id = None # This will be assigned by the database
        self.username = usr_data[0]
        self.password = usr_data[1]
        self.ingr_list = usr_data[2]
    def get_id(self):
        return str(self.id)

def getUserDataById(user_id):
    cur = conn.cursor()
    
    query = "SELECT usrname, pass, fridgelist FROM users WHERE usrid = %s"
    cur.execute(query, (user_id,))
    
    user_data = cur.fetchone()
    
    cur.close
    
    if user_data:
        return {
            'username': user_data[0],
            'password': user_data[1],
            'ingr_list': user_data[2],
        }
    return None
def getIdForNewUser(user):
    cur = conn.cursor
    
    query = "SELECT usrid FROM users WHERE username = %s"
    cur.execute(query, (user.username,))
    id = cur.fetchone()
    user.id = id
    cur.close()

def getUserByUsername(username):
    cur = conn.cursor
    
    query = "SELECT * FROM users WHERE username = %s"
    cur.execute(query, (username,))
    user = cur.fetchone()
    
    cur.close()
    return user

def insertUser(user):
    cur = conn.cursor
    query = "INSERT INTO users (usrname, pass, fridgelist) VALUES (%s, %s, %s)"
    cur.execute(query, (user.username, user.password, user.ingr_list))

    conn.commit()
    cur.close()
    