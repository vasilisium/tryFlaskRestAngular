from flask_restful import Resource
from backendApi import api, db
from config import Config
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(120), nullable=false)

    def __init__(self, username, email):
        self.username = username
        self.email = email

class HelloWorld(Resource):
    def get(self):
        # user = User("user1", "asd@asd.com");
        # user.add()
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/h')