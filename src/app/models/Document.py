from app.extensions import db
from datetime import datetime

#Tabela principal
class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    content = db.Column(db.Text)
    source_type = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    pdf_documents = db.relationship('PdfDocument', back_populates='document')

    def __init__(self, name: str, content: str, source_type: str):
        self.name = name
        self.content = content
        self.source_type = source_type