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
        
    def get_id(self, id):
        try:
            document = self.extractionService.get_id(id)

            if not document:
                return jsonify({"message": "Extração não encontrada."}), 404

            return jsonify({
                "id": document.id,
                "name": document.name,
                "content": document.content,
                "source_type": document.source_type
            }), 200

        except Exception as erro:
            return jsonify({"message": str(erro)}), 500
        
    def get_all(self):
        try:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 10))
            name = request.args.get("name")

            result = self.extractionService.get_all(page, limit, name)

            return jsonify(result), 200

        except Exception as erro:
            return jsonify({"message": str(erro)}), 500