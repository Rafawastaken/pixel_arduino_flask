from app import db

class PixelModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    coluna = db.Column(db.Integer, default = 0)
    linha = db.Column(db.Integer, default = 0)
    estado = db.Column(db.Integer, default = 0)