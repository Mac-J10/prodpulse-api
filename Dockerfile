FROM python:3.11-slim

# Install system deps & Rust toolchain
RUN apt-get update
RUN apt-get install -y curl build-essential pkg-config libssl-dev
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"
ENV CARGO_HOME="/root/.cargo"

# Create and activate a virtualenv
RUN python -m venv /venv
ENV PATH="/venv/bin:${PATH}"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

RUN pip install --upgrade pip
RUN  pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install --upgrade pip
RUN  pip install poetry
RUN  poetry config virtualenvs.create false
RUN  poetry install --no-dev --no-interaction --no-ansi

COPY . /app

# Collect static, run migrations if needed (optional)
# RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate

CMD ["gunicorn", "prodpulse_api.wsgi:application", "--bind", "0.0.0.0:8000"]