FROM python:3.13-alpine

# Install build dependencies and runtime libraries
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    musl-dev \
    gcc \
    python3-dev \
    cargo
# Copy application code
COPY . /app

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Set environment variables (adjust as needed)
ENV PATH=/root/.cargo/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LANGUAGE=C.UTF-8 \
    DJANGO_SETTINGS_MODULE=prodpulse_api.core.settings \
    PYTHONPATH=/app

# Expose port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "prodpulse_api.wsgi:application", "--bind", "0.0.0.0:8000"]
