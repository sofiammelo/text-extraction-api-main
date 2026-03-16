from flask import request
from app.services.ExampleService import ExampleService

class ExampleController:

    def __init__(self):
        self.exampleService = ExampleService

    # Crie um controlador onde define a chamada para service e retorno da resposta.
    def example_method(self):

        
        example_file = request.files['file']

        example = self.exampleService.example_method_service(
            example_file=example_file
        )

        return {
            "data": {
                "name": example.name,
                "text_file": example.text
            }
        }
