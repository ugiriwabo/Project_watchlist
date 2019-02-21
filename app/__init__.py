from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

#  Initializing application
app = Flask(__name__,instance_relative_config = True)
def create_app(config_name):
    app = Flask(__name__)
# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
bootstrap.init_app(app)
db.init_app(app)

from app import views
from app import error