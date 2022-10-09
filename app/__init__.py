from flask import Flask, render_template
from flask_restful import Api
from flask_restful import Resource, reqparse, abort, marshal_with, fields

app = Flask(__name__)

api = Api(app)

# Backen Api
communication_args = reqparse.RequestParser()


# Routes
@app.route('/')
def home():
    return render_template('home.html')