from flask import current_app
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def get_db():
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client.get_database()
    return db

def create_user(username, email, password):
    db = get_db()
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = {'username': username, 'email': email, 'password': hashed_password}
    db.users.insert_one(user)

def get_user_by_email(email):
    db = get_db()
    return db.users.find_one({'email': email})
