from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = '127.0.0.1'
port = os.environ['DB_PORT']
db_string = "postgres://" + str(user) + ":" + str(pwd) + "@" + str(host) + ":" + str(port) + "/" + str(db)

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']
host = 'postgres'
port = '1001'
engine = 'postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)

app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
