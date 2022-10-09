from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

from .routes.routes import fronted

app.register_blueprint(fronted, url_prefix="/")

