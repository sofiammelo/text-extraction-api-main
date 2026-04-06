from flask import Blueprint
from app.controllers.ExtractionController import ExtractionController

extractionController = ExtractionController()
extraction_routes = Blueprint("extractions", __name__)

extraction_routes.post("/extractions")(extractionController.extraction_method)
extraction_routes.get("/extractions/<id>")(extractionController.get_id)
extraction_routes.get("/extractions")(extractionController.get_all)