from flask import Blueprint
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from app import db
from app.routes.models import PixelModel

# Register blueprint
api_bp = Blueprint('api', __name__)

# Backen Api
communication_args = reqparse.RequestParser()
communication_args.add_argument('coluna', type=int, help="Coluna correspondente ao pixel", required=True)
communication_args.add_argument('linha', type=int, help="Linha correspondente ao pixel", required=True)
communication_args.add_argument('estado', type=int, help="Estado do pixel", required=True)

communication_args_patch = reqparse.RequestParser()
communication_args_patch.add_argument("id", type = int, help = "id do pixel")
communication_args_patch.add_argument('linha', type = int, help = "linha correspondente ao pixel")

communication_fields = {
    "coluna": fields.Integer,
    "linha": fields.Integer,
    "estado": fields.Integer
}

# Api
class PixelApi(Resource):
    @marshal_with(communication_fields)
    def get(self):
        pixels = PixelModel.query.all()
        return pixels