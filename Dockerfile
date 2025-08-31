FROM python:3.11-slim

# Install system deps & Rust toolchain
RUN apt-get update
RUN apt-get install -y \ 
    apt-utils ca-certificates curl build-essential pkg-config libssl-dev
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.cargo/bin:${PATH}"
ENV CARGO_HOME="/root/.cargo"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN  pip install "poetry==1.7.1"
RUN  poetry config virtualenvs.create false
RUN  poetry install --no-dev --no-interaction --no-ansi

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /app

# Collect static, run migrations if needed (optional)
# RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate
EXPOSE 8000
CMD ["gunicorn", "prodpulse_api.wsgi:application", "--bind", "0.0.0.0:8000"]