from . import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql, extensions
import psycopg2

import json


@login_manager.user_loader
def load_user(user_id):
    user_data = getUserDataById(user_id)
    if user_data:
        return User((user_data['id'], user_data['username'], user_data['password'], user_data['ingr_list']))
    return None
    
    
    


class User(tuple, UserMixin):
    def __init__(self, usr_data):
        self.id = usr_data[0]
        self.username = usr_data[1]
        self.password = usr_data[2]
        self.ingr_list = json.dumps(usr_data[3]) if len(usr_data) > 2 else '[]'
    def get_id(self):
        return str(self.id)
    def get_ingr_list(self):
        return json.loads(self.ingr_list)

def getUserDataById(user_id):
    cur = conn.cursor()
    query = "SELECT usrid, usrname, pass, fridgelist FROM users WHERE usrid = %s"
    cur.execute(query, (user_id,))
    
    user_data = cur.fetchone()
    
    cur.close
    
    if user_data:
        return {
            'id': user_data[0],
            'username': user_data[1],
            'password': user_data[2],
            'ingr_list': user_data[3],
        }
    return None
def getIdForNewUser(user):
    cur = conn.cursor()
    
    query = "SELECT usrid FROM users WHERE usrname = %s"
    cur.execute(query, (user.username,))
    id = cur.fetchone()
    user.id = id
    cur.close()

def getUserByUsername(username):
    cur = conn.cursor()
    
    query = "SELECT * FROM users WHERE usrname = %s"
    cur.execute(query, (username,))
    user_data = cur.fetchone()
    if user_data:
        usrid = user_data[0]
        usrname = user_data[1]
        passwrd = user_data[2]
        ingrlist = user_data[3]
        user = User((usrid, usrname, passwrd, ingrlist))
        cur.close
        return user
    cur.close()
    return None

def insertUser(user):
    cur = conn.cursor()
    query = "INSERT INTO users (usrid, usrname, pass, fridgelist) VALUES (%s, %s, %s, (ARRAY[]::text[]))"
    cur.execute(query, (user.id, user.username, user.password))

    conn.commit()
    cur.close()

def ingr_add_command(user_id, ingr_to_add):
    cur = conn.cursor()
    sql = """
    UPDATE users
    SET fridgelist = ARRAY_APPEND(fridgelist, LOWER(%s))
    WHERE usrid=%s AND NOT fridgelist @> ARRAY[%s];;
    """
    cur.execute(sql, (ingr_to_add,user_id, ingr_to_add))
    conn.commit()
    cur.close()

def ingr_remove_command(user_id, ingr_to_remove):
    cur = conn.cursor()
    sql = """
    Update users
    SET fridgelist = ARRAY_REMOVE(fridgelist, %s)
    WHERE usrid=%s;
    """
    cur.execute(sql, (ingr_to_remove,user_id))
    conn.commit()
    cur.close()

def recipe_match_request(user_id):
    cur = conn.cursor()
    sql = """
    SELECT recipename, rcplink from recipes
    WHERE ingr<@(SELECT fridgelist FROM users WHERE usrid=%s);
    """
    cur.execute(sql, (user_id,))
    result = cur.fetchall()
    cur.close()
    return result