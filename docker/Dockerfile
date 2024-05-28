FROM python:3.12-slim

# Install Poetry
RUN pip install poetry

# Copy project files
COPY . /app

# Copy AWS credentials JSON file
COPY ../credentials/aws_credentials.json /app/aws_credentials.json

# Set working directory
WORKDIR /app

# Install project dependencies 
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    poetry add boto3 google-cloud-bigquery

# Read AWS credentials from JSON file and set environment variables
RUN pip install jq
RUN AWS_ACCESS_KEY_ID=$(jq -r '.AWS_ACCESS_KEY_ID' /app/aws_credentials.json) \
    && AWS_SECRET_ACCESS_KEY=$(jq -r '.AWS_SECRET_ACCESS_KEY' /app/aws_credentials.json)

# Set environment variables for AWS
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY


# Run the script
CMD ["poetry", "run", "python", "src/crypto_datapipeline_executor.py"]
