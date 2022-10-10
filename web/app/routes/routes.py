from flask import render_template, Blueprint, redirect, request
from .models import PixelModel
from app import app, db

fronted = Blueprint("frontend", __name__)

@fronted.route('/')
def home():
    pixels = PixelModel.query.all()
    return render_template('home.html', pixels = pixels)