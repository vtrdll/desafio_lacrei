FROM python:3.12-slim

# Variáveis de ambiente (pegar do .env no docker-compose)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install --no-cache-dir poetry

# Desativa venv dentro do container
RUN poetry config virtualenvs.create false

# Copia arquivos de dependências
COPY pyproject.toml poetry.lock* ./

# Instala dependências
RUN poetry install --no-root --no-interaction --no-ansi

# Copia o restante do projeto
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
