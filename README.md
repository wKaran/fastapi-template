# FastAPI Template

A scalable FastAPI project template.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Create a new project](#1-create-a-new-project)
  - [2. Clone your repository](#2-clone-your-repository)
  - [3. Update project configuration](#3-update-project-configuration)
  - [4. Install dependencies](#4-install-dependencies)
  - [5. Activate the virtual environment](#5-activate-the-virtual-environment)
  - [6. Configure environment variables](#6-configure-environment-variables)
  - [7. Set up database migrations](#7-set-up-database-migrations)
  - [8. Run the application](#8-run-the-application)
- [Adding a New Module](#adding-a-new-module)
- [Running Tests](#running-tests)
- [License](#license)

## Features

- ⚡ **FastAPI** for a fast, modern, async-ready API layer
- 🏛️ **Clean Architecture** for clear separation of concerns
- 🗄️ **SQLAlchemy** ORM with **Alembic** migrations
- 📦 **uv** for fast, reliable dependency management

## Prerequisites

- Python 3.11+ (check `pyproject.toml` for the exact version)
- [uv](https://docs.astral.sh/uv/) installed
- A running database instance (e.g. PostgreSQL)

## Getting Started

### 1. Create a new project

On GitHub, click **Use this template → Create a new repository**, then name it after your project (e.g. `food-review-api`).

### 2. Clone your repository

```bash
git clone <your-new-repo-url>
cd <your-project-name>
```

### 3. Update project configuration

Open `pyproject.toml` and update the project metadata:

```toml
[project]
name = "food-review-api"
description = "FastAPI backend for food review system"
```

### 4. Install dependencies

```bash
uv sync
```

This will:

- Create a virtual environment (`.venv`)
- Install all dependencies
- Generate a lock file (`uv.lock`, if one doesn't already exist)

### 5. Activate the virtual environment

**Windows (Git Bash)**

```bash
source .venv/Scripts/activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 6. Configure environment variables

Copy the example environment file and fill in your own values (e.g. database URL, secrets):

```bash
cp .env.example .env
```

### 7. Set up database migrations

Initialize Alembic (skip this step if migrations are already set up in the template):

```bash
alembic init src/infrastructure/database/migrations
```

Then edit `src/infrastructure/database/migrations/env.py` to point Alembic at your models' metadata:

```python
from src.infrastructure.database.base import Base
from src.infrastructure.database import registry

target_metadata = Base.metadata
```

Generate and apply your first migration:

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 8. Run the application

```bash
fastapi dev src/main.py
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.


## Adding a New Module

Replace the sample module:

```text
src/modules/module_exp/
```

with your own feature modules, e.g.:

```text
src/modules/users/
src/modules/orders/
src/modules/workflows/
```

Each module typically follows the same internal Clean Architecture layers (domain, application, infrastructure, presentation) as the sample module.

---

🎯 **You're ready!** Start building your FastAPI backend 🚀