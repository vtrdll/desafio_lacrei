🛠️ Tecnologias Utilizadas

- Python 3.12
- Django 6.0
- Django Rest Framework
- JWT (SimpleJWT)
- PostgreSQL
- Poetry
- Pytest
- Black / Isort / Flake8
- corsheaders

⚙️ Pré-requisitos

- Python 3.12+
- Poetry instalado
- https://python-poetry.org/docs/#installation
- PostgreSQL (ou Docker)


▶️ Passo a passo para rodar o projeto (Docker)

### Passo 1️⃣ — Clonar o repositório
- git clone https://github.com/vtrdll/desafio_lacrei.git
- cd desafio_lacrei


### Passo 2️⃣ — Build da imagem Docker  (Durante o build, o Poetry é configurado para não criar virtualenv)
- docker compose build

### Passo 3️⃣ — Subir os containers (certifique-se se esta na raiz do projeto.)
- docker compose up
- docker-compose ps  #vereficase esta rodando. 

### Passo 4️⃣ — Rodar as migrações. (Criar Banco)
- docker compose exec web python manage.py migrate

### Passo 5️⃣ — Variáveis de Ambiente 
- Acesse .env.example e implemente variáveis de ambientes necessárias. Após isso  renomeie para .env

### Passo 6️⃣ — Criar superusuário
- docker compose exec web python manage.py createsuperuser (Isso dara permissão para acessar endpoints, não  esqueça do token)

### Passo 7️⃣— Autenticação JWT
- POST http://localhost:8000/api/token/ (username, password = criado em  superuser )
### Para acessar endpoints protegidos, inclua o token de acesso no header:
- Authorization: Bearer <token_de_acesso>

### Passo 8️⃣ — Acessar a aplicação 
http://localhost:8000

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


### Passo 9️⃣  — Rodar testes (Opicional. Os testes são feitos a cada push para o repositorio.)
-  docker compose exec web pytest
-  docker compose exec web black   
-  docker compose exec web isort
-  docker compose exec web flake8

============================================================================================================================

▶️ Passo a passo para rodar o projeto Setup local (sem Docker)
Este modo é recomendado apenas para desenvolvimento local.
Neste caso, o Poetry utilizará **ambiente virtual próprio**.

### Passo 1️⃣ - Pré-requisitos
- Python 3.12+
- Poetry
- PostgreSQL
- Git

### Passo 2️⃣ - Clonar o repositório
- git clone https://github.com/seu-usuario/seu-repositorio.git
- cd seu-repositorio

### Passo 3️⃣ - Criar ambiente virtual com Poetry
- poetry install
- poetry shell

### Passo 4️⃣ - Rodar migrações
- python manage.py migrate

### Passo 5️⃣ - Criar arquivo .env
- cp .env.example .env

### Passo 6️⃣ - Criar superusuário
- python manage.py createsuperuser (Isso dara permissão para acessar endpoints, não  esqueça do token)

### Passo 7️⃣ - Subir servidor local
- python manage.py runserver

### Passo 8️⃣ - Autenticação JWT
- POST http://localhost:8000/api/token/ (username, password = criado em  superuser )
### Para acessar endpoints protegidos, inclua o token de acesso no header:
- Authorization: Bearer <token_de_acesso>

Observação importante sobre o Poetry
Este projeto não utiliza poetry shell, pois:
virtualenvs.create = false
O container Docker já é o ambiente isolado
As dependências são instaladas diretamente no Python do container

===============================================================================================================

### ROLLBACK
Esta seção permite voltar o projeto para estado limpo, caso algo dê errado.

### ROLLBACK COMPLETO!
 
### docker compose down -v 
-   remove todos os containers definidos no docker-compose.yml e APAGA O BANCO DADOS.

### docker compose build --no-cache
-   recompila as imagens Docker do zero, ignorando qualquer cache anterior

### sobe aplicacao
-   docker compose up


Rollback apenas da aplicação sem alterar os volumes. 
### remove todos os containers definidos no docker-compose.yml
-   docker compose down

### sobe aplicacao
-   docker compose up

### Reset de migrações. Retornar a Zero permite uma nova aplicacao evitando conflitos
-   docker compose exec web python manage.py migrate app zero

### Criando nossa aplicacao 
-   docker compose exec web python manage.py migrate

### Limpeza total do Docker
-   docker system prune -af


### Observacoes importantes: 
-   Tenha  cuidado com a variável de ambiente DEBUG = FALSE  (producao).
ele controla parte  cruciais da configuracao do projeto.
-   Após a  criação, considere sempre que fazer alterações no banco de dados ou no settings.py utilizar python manage.py makemigrations (comando varia dependendo do ambiente) antes de cada migrate.py. Evite fazer esse  processo de forma descontrolada, podendo acarretar em conflito de migrações.
-   Caso queira pode alterar o time limit do token para durar mais tempo facilitando o desenvolvimento em settings.py.
-   .env.example contem mais detalhes sobre como estruturar sua .env

### PRINTS