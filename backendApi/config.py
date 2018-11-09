import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    db_connection_string ="postgresql://admin:1q2@localhost/balistica"
    # MONGO_URI = "mongodb://localhost:27017/crudT"
