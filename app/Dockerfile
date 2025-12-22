FROM python:3.12-slim

ENV DJANGO_SECRET_KEY=django-insecure-%reyouke64^6&%r2*)i0%dpq)xac3w+#ll%s0-70%$+6gescl4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# instala dependências do sistema (psycopg2 precisa disso)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# instala poetry
RUN pip install --no-cache-dir poetry

# DESATIVA venv (correto no Docker)
RUN poetry config virtualenvs.create false

# copia apenas arquivos de dependência (cache eficiente)
COPY pyproject.toml poetry.lock* ./

# instala dependências
RUN poetry install --no-root --no-interaction --no-ansi

# copia o restante do projeto
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
