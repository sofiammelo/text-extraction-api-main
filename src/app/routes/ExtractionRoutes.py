from flask import Blueprint
from app.controllers.ExtractionController import ExtractionController

extractionController = ExtractionController()
extraction_routes = Blueprint("extractions", __name__)

extraction_routes.post("/extractions")(extractionController.extraction_method)