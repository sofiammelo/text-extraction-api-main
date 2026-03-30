from flask import Flask
from app.config.database import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from app.extensions import db, migrate
from app.routes.ExtractionRoutes import extraction_routes

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    migrate.init_app(app, db)

    # Necessário importar as Models aqui.
    from app.models import Example
    from app.models import Example2
    from app.models import Document
    from app.models import PdfDocument

    # Registre as rotas aqui, igual no exemplo abaixo.
    app.register_blueprint(extraction_routes)

    return app
