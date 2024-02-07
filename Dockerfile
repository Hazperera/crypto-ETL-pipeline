# Use Python slim-buster as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python - \
    && apt-get remove -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Disable creation of virtual environments and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy the rest of your application's code
COPY . .

CMD ["python", "./etl.py"]

