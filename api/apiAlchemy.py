"""REID
   Create the API
"""

from flask import Flask
from resourceAlchemy import pieces, studios, evaluations

db_user = 'postgres'
# This is the password you set for 'postgres' user
db_password = 'flaskroot'

MYSQL_URI = f"postgresql://{db_user}:{db_password}@127.0.0.1/upmvideo"
# We link the database

def create_api():
    api = Flask(__name__)
    api.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_URI
    api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api.register_blueprint(pieces)
    api.register_blueprint(studios)
    api.register_blueprint(evaluations)

    return api