from werkzeug.datastructures import FileStorage
from app.models.Example import Example
from pypdf import PdfReader

# Aqui você importa o db, isso será necessário para salvar no banco de dados.
from app.extensions import db
class ExampleService:

    # Adicione a regra de negócios em uma "Service"
    def example_method_service(example_file: FileStorage) -> Example:
        reader = PdfReader(example_file.stream)

        for page in reader.pages:
            print(page.extract_text())

        # Aqui você vai criar o dado que será salvo no banco.
        example = Example(
            name="Example",
            text="RETORNE O TEXTO IGUAL NESSE EXEMPLO"
        )

        # Aqui você adiciona oque será salvo.
        db.session.add(example)
        # Aqui voce comita, e salva definitivamento no banco de dados.
        db.session.commit()

        return example