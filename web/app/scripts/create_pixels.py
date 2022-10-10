from app.routes.models import PixelModel
from app import db

def create_pixels():
    try:
        for coluna in range(1, 9):
            for linha in range(1, 9):
                new_pixel = PixelModel(
                    linha = linha,
                    coluna = coluna,
                    estado = 0
                )
                db.session.add(new_pixel)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False