import os

# Configuração do banco de dados.
SQLALCHEMY_DATABASE_URI = (
    "postgresql://"
    f"{os.getenv('DB_USER', 'extractions')}:"
    f"{os.getenv('DB_PASSWORD', 'extractions')}@"
    f"{os.getenv('DB_HOST', 'postgres')}:"
    f"{os.getenv('DB_PORT', '5432')}/"
    f"{os.getenv('DB_NAME', 'extractions')}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
