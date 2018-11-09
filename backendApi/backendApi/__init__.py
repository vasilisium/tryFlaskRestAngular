from flask import Flask
from flask_restful import Api
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.db_connection_string
db = SQLAlchemy(app)
api = Api(app)
app.config.from_object(Config)
app.debug = True

from backendApi import endpoints
from backendApi import routes