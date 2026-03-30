from app.extensions import db

# Example Tabela 2 de exemplo, relacionada com a Tabela Example
class Example2(db.Model):
    __tablename__ = 'examples2'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    example_id = db.Column(db.Integer, db.ForeignKey('examples.id'), nullable=False)

    example = db.relationship('Example', back_populates='example2s')

    def __init__(self, name: str, example_id: int):
        self.name = name
        self.example_id = example_id