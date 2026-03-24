from app.extensions import db

# Example Tabela principal
class Example(db.Model):
    __tablename__ = 'examples'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text)

    example2s = db.relationship('Example2', back_populates='example')

    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text
