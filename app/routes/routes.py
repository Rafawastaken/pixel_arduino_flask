from flask import render_template, Blueprint
from app import app

fronted = Blueprint("frontend", __name__)

@fronted.route('/')
def home():
    return render_template('home.html')