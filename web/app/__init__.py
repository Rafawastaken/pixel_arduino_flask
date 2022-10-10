from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__) # App object
db = SQLAlchemy(app) # Database object

# Local
from .routes.models import PixelModel
from .routes.routes import fronted
from .api.api import PixelApiGET, PixelApiPATCH, api_bp
from .scripts.create_pixels import create_pixels

# App Configs
app.config['SECRET_KEY'] = "randompass12333333"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'

# Create api obj
api = Api(api_bp)

# Routes
app.register_blueprint(fronted, url_prefix="/")
app.register_blueprint(api_bp)

# Api Endpoint
api.add_resource(PixelApiGET, '/update-matrix') # Get status of pixels
api.add_resource(PixelApiPATCH, '/post-matrix/<int:id_pixel>') # Change status of pixel

# Create tables
db.create_all()

# Check if pixeis
pixels = PixelModel.query.all()
if not pixels:
    status = create_pixels()
    if status: print("Pixels criados com sucesso! ")
    else: print("Impossivel criar pixels")