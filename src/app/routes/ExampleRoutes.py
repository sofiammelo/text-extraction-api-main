from flask import Blueprint
from app.controllers.ExampleController import ExampleController

# Esse exemplo é para usar como base, deve ser criado outro arquivo para a suas rotas, use como base esse aqui.
exampleController = ExampleController()

example_routes = Blueprint("examples", __name__)

example_routes.post("/examples")(exampleController.example_method)
