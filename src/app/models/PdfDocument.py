from app.extensions import db

class PdfDocument(db.Model):
    __tablename__ = 'pdf_documents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'), nullable=False)

    document = db.relationship('Document', back_populates='pdf_documents')

    def __init__(self, name: str, document_id: int):
        self.name = name
        self.document_id = document_id