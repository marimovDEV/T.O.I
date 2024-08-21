import sqlite3
from config import BAZA

def insert_user(full_name,telegram_id,username,created_at):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO main_users (full_name,telegram_id,username,created_at) VALUES (?,?,?,?)', (full_name,telegram_id,username,created_at))
        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
    except:
        pass
    
def get_user():
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_users')
    users = cursor.fetchall()
    
    lst = []
    
    for user in users: 
        lst.append(user[1])
       
    return lst

def get_admin()-> list:
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_bot_admin')
    admins = cursor.fetchall()
    
    lst=[]
    

    
    for admin in admins:
        
            
        lst.append(admin[1])
    
    return lst
    
def insert_client(loyiha,full_name,phone_number,created_at):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()
    
    
    cursor.execute('INSERT INTO main_clients (loyiha,full_name,phone_number,created_at) VALUES (?,?,?,?)', (loyiha,full_name,phone_number,created_at))
    connection.commit()
    connection.close()
    
def insert_admin(full_name,telegram_id,username):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()
    
    
    cursor.execute('INSERT INTO main_bot_admin (full_name,telegram_id,username) VALUES (?,?,?)', (full_name,telegram_id,username))
    connection.commit()
    connection.close()
    

    
    
    