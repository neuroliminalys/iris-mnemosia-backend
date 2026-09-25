# BACKEND

## Start command

To start the server, run : ```poetry run uvicorn src.iris_mnemosia_backend.main:app --reload```

To create initial database migration : ```poetry run alembic revision --autogenerate -m "initial"```

To apply the migration : ```poetry run alembic upgrade head```

To upgrade database : ```poetry run alembic revision --autogenerate -m "initial"``` then apply the migration

## Endpoints

- `/status/api` : returns `{"status": "ok"}` if the API is working
- `/status/database` : returns `{"status": "ok"}` if the database is working
