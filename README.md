# Roles Project

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-282C34?style=flat&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/) [![Alembic](https://img.shields.io/badge/Alembic-4E98E8?style=flat&logo=alembic&logoColor=white)](https://alembic.sqlalchemy.org/en/latest/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/) [![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat&logo=docker&logoColor=white)](https://docs.docker.com/compose/) [![Pydantic](https://img.shields.io/badge/Pydantic-2B7DBC?style=flat&logo=python&logoColor=white)](https://pydantic-docs.helpmanual.io/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-2B7DBC?style=flat&logo=python&logoColor=white)](https://www.uvicorn.org/) [![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/) [![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/) [![Swagger UI](https://img.shields.io/badge/Swagger_UI-85EA2D?style=flat&logo=swagger&logoColor=black)](https://swagger.io/tools/swagger-ui/) [![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)](https://www.markdownguide.org/)

## Installation

### Pre-requisites :clipboard:

- VsCode (with Dev Containers Extension)
- Git
- Add a `.env` file in the .devcontainer folder with the following variables:
```env
ENVIRONMENT="local"
PG_DB_NAME="rools_db"
PG_USERNAME="appuser"
PG_PASSWORD="apppassword"
PG_HOSTNAME="localhost"
PG_PORT=5432
```

## Getting Started :wrench:
1. Open project in dev container   
   - VsCode Command Palette: `Dev Containers: Reopen in Container

2. Project start:
   - Fast API starts on https://localhost:8000 
   - PgAdmin starts on https://localhost:8080


## Additional Available Commands

**Starting the application in development mode:**
```bash
fastapi dev main.py
```

**create_migration**

```bash
alembic revision --autogenerate -m 'migration message'
```

**migrate**

```bash
alembic upgrade head
```
**downgrade**

```bash
alembic downgrade -1
```

#### Connecting dev container to GitHub Repo :link:
1. Authenticate GitHub CLI:

```bash
   gh auth login.  
```

2. Verify remote URL:

```bash
   git remote -v
```

3. If needed, set the correct remote URL:
   
```bash
   git remote set-url origin https://github.com/Madeeha-Anjum/roles.git
```

#### Container commands :mag:
- List all running containers and read the container ID
```bash
   docker ps
```   

- View the logs of the container:
```bash
docker logs <container_id>
```
- Run interactively inside the container:
```bash
docker exec -it <container_id> /bin/bash
```

#### Postgres database access 
```bash
docker exec -it <container_id> 
psql -U appuser -d rools_db
```