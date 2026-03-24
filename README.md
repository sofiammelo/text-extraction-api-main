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

# Iniciar o projeto com docker

Se for sistema Windows, necessário instalar WSL2 e docker.

## Iniciar o projeto com docker

```bash
docker compose up -d
```

## Encerrar o projeto com docker

```bash
docker compose down
```

## Listar os container desse projeto

```bash
docker compose ps
```

### Se estiver rodando deve ver algo assim

```bash
NAME                       IMAGE                     COMMAND                  SERVICE    CREATED              STATUS              PORTS
text-extraction-app        text-extraction-api-app   "python ./src/main.py"   app        About a minute ago   Up About a minute   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp
text-extraction-postgres   postgres:18.1-alpine      "docker-entrypoint.s…"   postgres   About a minute ago   Up About a minute   0.0.0.0:5435->5432/tcp, [::]:5435->5432/tcp
```

### Se não estiver rodando deve ver algo assim

```bash
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
```
