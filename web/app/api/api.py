from flask import Blueprint
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields

# Register blueprint
api_bp = Blueprint('api', __name__)

# Backen Api
communication_args = reqparse.RequestParser()
communication_args.add_argument('linha', type=int, help="Linha correspondente ao pixel", required=True)
communication_args.add_argument('coluna', type=int, help="Coluna correspondente ao pixel", required=True)
communication_args.add_argument('estado', type=int, help="Estado do pixel", required=True)

communication_fields = {
    "linha": fields.Integer,
    "coluna": fields.Integer,
    "estado": fields.Integer
}

# Api
class Pixel(Resource):
    @marshal_with(communication_fields)
    def get(self):
        return "get_req"