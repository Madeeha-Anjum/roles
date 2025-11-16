# Roles

## Available Commands

**create venv (Linux/Mac)**

```bash
python3 -m venv .venv

```

**activate venv (Linux/Mac)**

```bash
source .venv/bin/activate
```

**install dependencies (Linux/Mac)**

```bash
 pip3 install -r requirements.txt 
```

**start**

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
