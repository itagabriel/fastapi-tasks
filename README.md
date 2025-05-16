# FastAPI Tasks

Este projeto é uma aplicação de gerenciamento de tarefas (TODO) desenvolvida com FastAPI, SQLAlchemy e PostgreSQL, com suporte a Docker.

## Funcionalidades

- Criar novas tarefas
- Listar todas as tarefas existentes
- Atualizar tarefas existentes
- Excluir tarefas
- Middleware de CORS habilitado para desenvolvimento frontend

## Estrutura do Projeto

```
project_fastapi/
├── app/
│   ├── main.py         # Rotas e lógica principal da aplicação
│   ├── models.py       # Definição do modelo de dados (ORM)
│   ├── schemas.py      # Schemas para validação com Pydantic
│   └── database.py     # Configuração de banco de dados
│
├── Dockerfile          # Dockerfile da aplicação
├── docker-compose.yml  # Orquestração com PostgreSQL
├── requirements.txt    # Dependências do projeto
├── wait-for-it.sh      # Script para aguardar o banco iniciar
└── README.md           # Documentação do projeto
```

## Requisitos

- Docker
- Docker Compose

## Instruções para execução com Docker

Clone o repositório e inicie os serviços:

```bash
git clone https://github.com/itagabriel/fastapi-tasks.git
cd fastapi-tasks
docker-compose up --build
```

A API estará disponível em: `http://localhost:8000`  
Documentação interativa: `http://localhost:8000/docs`

## Endpoints da API

### GET /
Verifica se a API está ativa.

### GET /tasks
Retorna todas as tarefas cadastradas.

### POST /tasks
Cria uma nova tarefa.

Exemplo de corpo JSON:
```json
{
  "title": "Nome da tarefa",
  "done": false
}
```

### PUT /tasks/{id}
Atualiza os dados de uma tarefa existente.

### DELETE /tasks/{id}
Exclui uma tarefa com base no ID.

## Configuração de ambiente

A variável de ambiente `DATABASE_URL` pode ser utilizada para configurar a URL de conexão com o banco de dados.

Exemplo:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/todo_db
```

## Execução local (sem Docker)

Instale as dependências:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Licença

Este projeto está licenciado sob os termos da licença MIT.