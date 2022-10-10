from flask import Blueprint
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from app import db
from app.routes.models import PixelModel

# Register blueprint
api_bp = Blueprint('api', __name__)

# Backen Api
communication_args = reqparse.RequestParser()
communication_args.add_argument("id", type=int, help="ID do pixel", required = True)
communication_args.add_argument('coluna', type=int, help="Coluna correspondente ao pixel", required=True)
communication_args.add_argument('linha', type=int, help="Linha correspondente ao pixel", required=True)
communication_args.add_argument('estado', type=int, help="Estado do pixel", required=True)

communication_args_patch = reqparse.RequestParser()
communication_args_patch.add_argument("estado", type = str, help = "id do pixel", required = True)


communication_fields_get = {
    "id":fields.Integer,
    "coluna": fields.Integer,
    "linha": fields.Integer,
    "estado": fields.Integer
}

communication_fields_patch = {
    "estado": fields.Integer
}

# Api
class PixelApiGET(Resource):
    @marshal_with(communication_fields_get)
    def get(self):
        pixels = PixelModel.query.all()
        return pixels

class PixelApiPATCH(Resource):
    @marshal_with(communication_fields_patch)
    def post(self, id_pixel):
        args = communication_args_patch.parse_args()
        pixel = PixelModel.query.filter_by(id = id_pixel).first()

        if not pixel: abort(404, message = "Pixel não encontrado")
        if args['estado']:
            print(type(args['estado']))
            if args['estado'] == "0": pixel.estado = 0
            elif args['estado'] == "1": pixel.estado = 1
            else: abort(400, message = "Estado nao suportado")
            db.session.commit()
        return pixel