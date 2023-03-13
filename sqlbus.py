import sqlite3


conn=sqlite3.connect("db/users.db")
cursor=conn.cursor()

def db_create_user(user_id: int, latitude: float, longitude: float):
    cursor.execute('INSERT INTO  users(user_id, latitude, longitude) VALUES (?,?,?)',(user_id, latitude, longitude))
    conn.commit()