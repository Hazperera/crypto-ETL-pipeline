FROM python:3.12-slim

# Install Poetry
RUN pip install poetry

# Copy project files
COPY . /app

# Set working directory
WORKDIR /app

# Install project dependencies 
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    poetry add google-cloud-bigquery


# Run the script
# CMD ["poetry", "run", "python", "bq_to_parquet.py"]

