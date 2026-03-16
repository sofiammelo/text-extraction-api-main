# text-extraction-api

## Requisitos

- Python 3.10+

## Configuração do ambiente

**1. Criar o ambiente virtual:**

```bash
python3 -m venv .venv
```

**2. Ativar o ambiente virtual:**

```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**3. Instalar as dependências:**

```bash
pip install -r requirements.txt
```

## Iniciando o projeto

```bash
python src/main.py
```

A API estará disponível em `http://localhost:8081`.


## Escopo para ser usado como base

1. **Criar um novo arquivo de rotas** na pasta `src/app/routes/`.  
   Use o `ExampleRoutes.py` como referência para criar o novo arquivo.

   - Defina o **path da rota**, por exemplo: `"/examples"`.
   - Defina a rota utilizando o método **POST**. No `ExampleRoutes.py` o exemplo está utilizando **POST**, então siga como exemplo `example_routes.post(...)`.
   - Registre a rota no `main.py`. Use como exemplo o registro que é feito com o `ExampleRoutes.py`.

2. **Defina um controlador**, seguindo o `ExampleController.py`.  
   Crie um novo arquivo em `src/app/controllers/`, que será responsável por receber a requisição da rota **POST** definida no arquivo criado em `src/app/routes/`.

3. **Crie um serviço**, seguindo o `ExampleService.py`.  
   Crie um novo arquivo em `src/app/services/`. Esse arquivo será responsável pelas **validações** e pelo **tratamento da extração do texto do PDF**.

   - Nesse arquivo vocês **DEVEM utilizar o código que já criaram**.
   - Porém, **não apenas copiem e colem**. Usem o código como base para **abstrair e organizar a lógica** dentro desse novo arquivo de serviço.
   - Utilizem o `ExampleService.py` como referência.

4. **Crie uma entidade (ou modelo)** utilizando o `Example.py`, que está na pasta `src/app/models/`.

   - Crie uma representação do documento, contendo algo como:
     - `name` → nome do arquivo  
     - `content` → conteúdo extraído do arquivo

5. **Resposta da API**

   Retorne a resposta da API da mesma forma que no `ExampleController`, utilizando `jsonify`, seguindo o exemplo, mas retornando o **texto que foi extraído do arquivo PDF**.

## Considerações

- Considerem ver como enviar arquivo para API com flask [Click aqui para ver Upload de Arquivo para API com Flask](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/#a-gentle-introduction)
- Python com Orientação ao Objeto, [Clique aqui para se ter uma base](https://www.treinaweb.com.br/blog/orientacao-a-objetos-em-python?utm_source=google&utm_medium=pmax&utm_campaign=home-A-iniciantes&utm_source=&utm_medium=&utm_campaign=&utm_content=&gad_source=1&gad_campaignid=22076590256&gclid=CjwKCAjw687NBhB4EiwAQ645dkv3tWEV9N33L0EjU-B9v9e6nkeHOCCGsYo_EIPc9LehJppSDXXOrhoCUhEQAvD_BwE).
- Utilização de JSON para resposta de API