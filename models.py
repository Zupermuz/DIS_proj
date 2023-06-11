#from bank import conn, login_manager
#from flask_login import UserMixin

from psycopg2 import sql

def get_fridge_content(usrid):
    from app import get_db_connection
    conn = get_db_connection()
    cur = conn.cursor()
    sql = """
    SELECT usrname, fridgelist FROM users
    WHERE usrid = %s;
    """
    cur.execute(sql, (usrid,))
    fridge = cur.fetchall()
    cur.close()
    conn.close()
    return fridge

def add_fridge_item(usrid, food):
    from app import get_db_connection
    conn = get_db_connection()
    cur = conn.cursor()
    sql = """
    UPDATE users
    SET fridgelist = array_append(fridgelist, %s);
    """
    cur.execute(sql, (food,))
    conn.commit()
    cur.close()
    conn.close()