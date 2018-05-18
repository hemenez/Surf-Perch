from flask import Flask

app = Flask(__name__)

from app import routes

from models.engine import db_storage
storage = db_storage.DBStorage()
storage.reload()
