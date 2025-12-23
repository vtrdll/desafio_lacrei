🛠️ Tecnologias Utilizadas

Python 3.12
Django 6.0
Django Rest Framework
JWT (SimpleJWT)
PostgreSQL
Poetry
Pytest
Black / Isort / Flake8


⚙️ Pré-requisitos

Python 3.12+
Poetry instalado
https://python-poetry.org/docs/#installation
PostgreSQL (ou Docker)


▶️ Passo a passo para rodar o projeto (Docker)

1️⃣ Passo  — Pré-requisitos
docker --version
docker compose version
git --version


2️⃣ Passo  — Clonar o repositório
git clone https://github.com/vtrdll/desafio_lacrei.git
cd desafio_lacrei


3️⃣ Passo  — Variáveis de Ambiente (.env)
DEBUG=True
SECRET_KEY=django-insecure-troque-esta-chave-disponivel-em-settings.py
POSTGRES_DB=app_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=app_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
ALLOWED_HOSTS=localhost 127.0.0.1


4️⃣ Passo  — Build da imagem Docker
Durante o build, o Poetry é configurado para não criar virtualenv:
docker compose build


5️⃣ Passo  — Subir os containers
docker compose up


6️⃣ Passo  — Rodar as migrações
docker compose exec web python manage.py migrate


7️⃣ Passo  — Criar superusuário
docker compose exec web python manage.py createsuperuser


8️⃣ Passo  — Acessar a aplicação
http://localhost:8000


9️⃣ Passo  — Autenticação JWT
Obter token:
POST /api/token/
Refresh do token:
POST /api/token/refresh/


🔟 Passo  — Rodar testes
docker compose exec web pytest

1️⃣1️⃣ Passo  — Padronização de código
docker compose exec web black .
docker compose exec web isort .
docker compose exec web flake8

=====================================

Observação importante sobre o Poetry

Este projeto não utiliza poetry shell, pois:
virtualenvs.create = false
O container Docker já é o ambiente isolado
As dependências são instaladas diretamente no Python do container

=====================================

Rollback
Esta seção permite voltar o projeto para estado limpo, caso algo dê errado.

Rollback completo
docker compose down -v
docker compose build --no-cache
docker compose up

Rollback apenas da aplicação
docker compose down
docker compose up

Reset de migrações
docker compose exec web python manage.py migrate app zero
docker compose exec web python manage.py migrate

Limpeza total do Docker
docker system prune -af


▶️ Passo a passo para rodar o projeto Setup local (sem Docker)
Este modo é recomendado apenas para desenvolvimento local.
Neste caso, o Poetry utilizará **ambiente virtual próprio**.


1️⃣ Pré-requisitos
- Python 3.12+
- Poetry
- PostgreSQL
- Git


2️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


3️⃣ Criar ambiente virtual com Poetry
poetry install
poetry shell


4️⃣ Criar arquivo .env
cp .env.example .env


5️⃣ Rodar migrações
python manage.py migrate


6️⃣ Criar superusuário
python manage.py createsuperuser


7️⃣ Subir servidor local
python manage.py runserver


### EndPoint Profissionais
- `GET /api/profissionais/` → lista
- `GET /api/profissionais/{id}/` → consulta por id
- `POST /api/profissionais/` → cria  
- `PUT /api/profissionais/{id}/` → atualiza
- `DELETE /api/profissionais/{id}/` → remove

### EndPoint Consultas
- `GET /api/consultas/` → lista
- `GET /api/consultas/{id}/` → consulta por id
- `POST /api/consultas/` → cria  (passar id do profissional)
- `PUT /api/consultas/{id}/` → atualiza
- `DELETE /api/consultas/{id}/` → remove

Esse foi meu primeiro desafio. Enfretei dificuldades nunca vistas constribuiu muito para meu arsenal. 