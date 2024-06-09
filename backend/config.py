# contains the configurations for the project

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# now we can send cross origin requests with out any errors
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # disbacling just for development purposes

# create a DB instance which will give access to the DB to do CRUD operations
db = SQLAlchemy(app)

