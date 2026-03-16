from werkzeug.datastructures import FileStorage
from app.models.Example import Example
from pypdf import PdfReader

class ExampleService:

    # Adicione a regra de negócios em uma "Service"
    def example_method_service(example_file: FileStorage) -> Example:
        reader = PdfReader(example_file.stream)

        for page in reader.pages:
            print(page.extract_text())

        example = Example(
            name="Example",
            text="RETORNE O TEXTO IGUAL NESSE EXEMPLO"
        )

        return example