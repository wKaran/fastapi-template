# Getting Started

## 1. Initialize the project

```bash
uv init <project-name>
cd <project-name>
```

## 2. Create a virtual environment

```bash
uv venv
```

Activate it:

**Windows (Git Bash)**

```bash
source .venv/Scripts/activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

## 3. Install dependencies

Install the required packages for your project.

Example:

```bash
uv add fastapi uvicorn sqlalchemy alembic pydantic-settings
```

## 4. Initialize Alembic

```bash
alembic init src/infrastructure/database/migrations
```

## 5. Configure Alembic

Open:

```text
src/infrastructure/database/migrations/env.py
```

Import your SQLAlchemy base and model registry:

```python
from src.infrastructure.database.base import Base
from src.infrastructure.database import registry

target_metadata = Base.metadata
```

## 6. Start building

Create your first feature by replacing:

```text
src/modules/module_exp/
```

with your own module, for example:

```text
src/modules/users/
src/modules/orders/
src/modules/workflows/
```