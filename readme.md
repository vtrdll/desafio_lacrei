<h1 align="center"> Desafio Lacrei — API Django</h1>

<p align="center">
  <b>API REST construída com Django + DRF, autenticação JWT e PostgreSQL</b>
</p>

<hr/>

<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.12</li>
  <li>Django 6.0</li>
  <li>Django Rest Framework</li>
  <li>JWT (SimpleJWT)</li>
  <li>PostgreSQL</li>
  <li>Poetry</li>
  <li>Pytest</li>
  <li>Black / Isort / Flake8</li>
  <li>corsheaders</li>
  <li>Docker & Docker Compose</li>
</ul>

<hr/>

<h2>⚙️ Pré-requisitos</h2>
<ul>
  <li>Python 3.12+</li>
  <li>Poetry instalado</li>
  <li>
    Documentação:
    <a href="https://python-poetry.org/docs/#installation" target="_blank">
      https://python-poetry.org/docs/#installation
    </a>
  </li>
  <li>PostgreSQL (ou Docker)</li>
</ul>

<hr/>

<h2>▶️ Executando o Projeto com Docker (Recomendado)</h2>

<h3>1️⃣ Clonar o repositório</h3>
<pre><code>git clone https://github.com/vtrdll/desafio_lacrei.git
cd desafio_lacrei</code></pre>

<h3>2️⃣ Build da imagem Docker</h3>
<p>Durante o build, o Poetry é configurado para <b>não criar virtualenv</b>.</p>
<pre><code>docker compose build</code></pre>

<h3>3️⃣ Subir os containers</h3>
<pre><code>docker compose up
docker compose ps</code></pre>

<h3>4️⃣ Rodar as migrações</h3>
<pre><code>docker compose exec web python manage.py migrate</code></pre>

<h3>5️⃣ Variáveis de Ambiente</h3>
<ul>
  <li>Acesse <code>.env.example</code></li>
  <li>Implemente as variáveis necessárias</li>
  <li>Renomeie para <code>.env</code></li>
</ul>

<h3>6️⃣ Criar superusuário</h3>
<pre><code>docker compose exec web python manage.py createsuperuser</code></pre>
<p><i>Esse usuário será usado para autenticação JWT.</i></p>

<h3>7️⃣ Autenticação JWT</h3>
<pre><code>POST http://localhost:8000/api/token/</code></pre>

<p>Headers para endpoints protegidos:</p>
<pre><code>Authorization: Bearer &lt;token_de_acesso&gt;</code></pre>

<h3>8️⃣ Acessar a aplicação</h3>
<p>
  👉 <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>
</p>

<hr/>

<h2>📌 Endpoints Disponíveis</h2>

<h3>👨‍⚕️ Profissionais</h3>
<ul>
  <li><code>GET /api/profissionais/</code> → Listar</li>
  <li><code>GET /api/profissionais/{id}/</code> → Consultar por ID</li>
  <li><code>POST /api/profissionais/</code> → Criar</li>
  <li><code>PUT /api/profissionais/{id}/</code> → Atualizar</li>
  <li><code>DELETE /api/profissionais/{id}/</code> → Remover</li>
</ul>

<h3>📅 Consultas</h3>
<ul>
  <li><code>GET /api/consultas/</code> → Listar</li>
  <li><code>GET /api/consultas/{id}/</code> → Consultar por ID</li>
  <li><code>POST /api/consultas/</code> → Criar (informar ID do profissional)</li>
  <li><code>PUT /api/consultas/{id}/</code> → Atualizar</li>
  <li><code>DELETE /api/consultas/{id}/</code> → Remover</li>
</ul>

<hr/>

<h2>🧪 Testes & Qualidade de Código (Opcional)</h2>
<p>Os testes são executados via GitHub Actions.</p>

<pre><code>docker compose exec web pytest
docker compose exec web black
docker compose exec web isort
docker compose exec web flake8</code></pre>

<hr/>

<h2>▶️ Setup Local (Sem Docker)</h2>
<p><b>Recomendado apenas para desenvolvimento local.</b></p>

<h3>Pré-requisitos</h3>
<ul>
  <li>Python 3.12+</li>
  <li>Poetry</li>
  <li>PostgreSQL</li>
  <li>Git</li>
</ul>

<h3>Passos</h3>
<pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
poetry install
poetry shell
python manage.py migrate
cp .env.example .env
python manage.py createsuperuser
python manage.py runserver</code></pre>

<hr/>

<h2>♻️ ROLLBACK & RESET</h2>

<h3>🔥 Rollback Completo (Remove Banco)</h3>
<pre><code>docker compose down -v
docker compose build --no-cache
docker compose up</code></pre>

<h3>♻️ Rollback Apenas da Aplicação</h3>
<pre><code>docker compose down
docker compose up</code></pre>

<h3>🗄️ Reset de Migrações</h3>
<pre><code>docker compose exec web python manage.py migrate app zero
docker compose exec web python manage.py migrate</code></pre>

<h3>🧹 Limpeza Total do Docker</h3>
<pre><code>docker system prune -af</code></pre>

<hr/>

<h2>⚠️ Observações Importantes</h2>
<ul>
  <li>
    ⚠️ Atenção à variável <code>DEBUG = FALSE</code> (produção).
    Ela controla partes críticas da aplicação.
  </li>
  <li>
    Sempre que alterar models ou <code>settings.py</code>, execute:
    <code>makemigrations</code> antes de <code>migrate</code>.
  </li>
  <li>
    Evite rodar migrações de forma descontrolada para não gerar conflitos.
  </li>
  <li>
    O tempo de expiração do token JWT pode ser ajustado em <code>settings.py</code>.
  </li>
  <li>
    Consulte o <code>.env.example</code> para entender todas as variáveis disponíveis.
  </li>
</ul>

<hr/>

<p align="center">
  🚀 <b>Projeto pronto para desenvolvimento, testes e deploy!</b>
</p>
