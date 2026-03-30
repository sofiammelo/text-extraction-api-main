from flask import request, jsonify
from app.services.ExtractionService import ExtractionService

class ExtractionController:

    def __init__(self):
        self.extractionService = ExtractionService()

    def extraction_method(self):
        try:    
            pdf_recebido = request.files["file"]

            document = self.extractionService.extraction_method_service(
                pdf_file = pdf_recebido
            )

            return jsonify({
                "message": document.content
            }), 200
        
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), 500