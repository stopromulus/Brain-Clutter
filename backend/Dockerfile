FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=TRUE

# install & configure poetry
RUN python3 -m pip install poetry --no-cache-dir
RUN poetry config virtualenvs.in-project true

WORKDIR /Brain-Clutter/backend

# install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev --no-interaction

# copy over necessary files
COPY . .

# run app
CMD poetry run gunicorn backend.wsgi -b 0.0.0.0:8000
