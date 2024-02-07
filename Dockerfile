# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary files for installing dependencies
COPY pyproject.toml poetry.lock* ./

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure Poetry:
# Disable the creation of virtual environments because
# the Docker container itself provides isolation
RUN poetry config virtualenvs.create false

# Install project dependencies
# This step uses pyproject.toml and poetry.lock to install dependencies
RUN poetry install --no-dev

# Copy the rest of your application's code
# COPY 

# Run the Python script on container startup
CMD ["python", "./main.py"]

