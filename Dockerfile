# Stage 1: Install Poetry
# Use an intermediate image to install poetry
FROM python:3.12-slim as poetry-base
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python -

# Stage 2: Build the application image
FROM python:3.12-slim as builder
WORKDIR /app

# Copy only files necessary for installing dependencies
COPY --from=poetry-base /usr/local/bin/poetry /usr/local/bin/poetry
COPY pyproject.toml poetry.lock* ./

# Disable creation of virtual environments and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Stage 3: Run the application
FROM python:3.12-slim as runtime
WORKDIR /app

# Copy installed packages from the builder image
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY . .


CMD ["python", "./etl.py"]
