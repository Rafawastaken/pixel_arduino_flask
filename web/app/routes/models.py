from app import db

class PixelModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    coluna = db.Column(db.Integer, default = 0)
    linha = db.Column(db.Integer, default = 0)
    estado = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return f"Pixel(linha = {self.linha}, coluna = {self.coluna}, estado = {self.estado})"

db.create_all()# Criar modelo