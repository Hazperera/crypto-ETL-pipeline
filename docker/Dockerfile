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
    poetry add boto3 google-cloud-bigquery

# Set environment variables for AWS and Google Cloud credentials 
ENV AWS_ACCESS_KEY_ID=ccc
ENV AWS_SECRET_ACCESS_KEY=ccc

# Run the script
CMD ["poetry", "run", "python", "src/crypto_datapipeline_executor.py"]
