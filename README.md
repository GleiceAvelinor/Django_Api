🧩 Projeto API Django
Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework. Ele serve como base para aplicações web que exigem autenticação, gerenciamento de dados e documentação interativa via Swagger.

🚀 Tecnologias Utilizadas
Python 3.x

Django

Django REST Framework

drf-yasg — Geração de documentação Swagger/OpenAPI

📁 Estrutura do Projeto
Código
api/
├── api/                # Configurações principais do projeto
│   ├── settings.py     # Arquivo de configuração (você está aqui!)
│   ├── urls.py         # Rotas principais
│   └── wsgi.py         # Interface WSGI
├── minha_api/          # Aplicativo principal da API
│   ├── models.py       # Modelos de dados
│   ├── views.py        # Lógicas de negócio
│   ├── serializers.py  # Serializadores DRF
│   └── urls.py         # Rotas específicas da API
└── manage.py           # Utilitário de linha de comando do Django
⚙️ Configuração Inicial
Clone o repositório:

bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Execute as migrações:

bash
python manage.py migrate
Inicie o servidor de desenvolvimento:

bash
python manage.py runserver
📚 Documentação da API
Após iniciar o servidor, acesse:

Swagger UI: http://localhost:8000/swagger/

Redoc: http://localhost:8000/redoc/

🔐 Autenticação
A API pode ser configurada para usar autenticação via token, JWT ou sessão. Consulte a documentação do Django REST Framework para mais detalhes.

🧪 Testes
Para rodar os testes automatizados:

bash
python manage.py test
🌍 Configurações Regionais
Idioma: pt-br

Fuso horário: America/Sao_Paulo

📄 Licença
Este projeto está licenciado sob os termos da MIT License.
