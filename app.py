from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:""@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false

SQLAlchemy(app)