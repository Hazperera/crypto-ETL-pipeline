# Crypto ETL Pipeline

## Overview

This repository contains a data pipeline that processes cryptocurrency data using Google BigQuery and uploads the processed data to an AWS S3 bucket. The pipeline consists of multiple scripts to handle different parts of the ETL (Extract, Transform, Load) process.

## Files

- `crypto_bigquery_data_processing.py`

   Fetches data from Google BigQuery and writes the results to Parquet files.

- `crypto_localstack_s3_data_loader.py`

   Uploads the Parquet files generated by the BigQuery processing script to an AWS S3 bucket.

-  `crypto_datapipeline_executor.py`

   Orchestrates the execution of the `crypto_bigquery_data_processing.py` and `crypto_localstack_s3_data_loader.py` scripts.

## Usage

### Environment Setup

1. **Set up your environment**: Ensure the necessary environment variables are set for AWS access keys.

### Running Locally

1. **Environment Setup:**
   - Make sure you have Python 3.12 installed on your system.
   - Set up a virtual environment for the project to manage dependencies.
   - Install Poetry, a dependency management tool:
     ```bash
     pip install poetry
     ```

2. **Clone the Repository:**
   - Use the following commands to clone the repository and change to the directory:
     ```bash
     git clone <repository_url>
     cd <repository_directory>
     ```

3. **Install Dependencies:**
   - Install project dependencies with Poetry:
     ```bash
     poetry install
     ```
      #### Dependencies
      - google-cloud-bigquery
      - pandas
      - boto3
      - botocore


4. **Run the Data Pipeline:**
   - To execute the main Python script:
     - First, activate the Poetry shell:
     ```bash
     poetry shell 
     ```
     - Set the environment variable for Google credentials:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
     ```
     - Run the script:
     ```bash
     python crypto_datapipeline_executor.py
     ```
### Running on the Cloud

1. **Set up your environment**: Ensure your cloud environment is configured correctly with the necessary credentials and permissions.

2. **Deploy the Scripts**: Depending on your cloud provider, you may need to deploy the scripts to a virtual machine, container, or a managed service. Ensure the necessary environment variables are set for Google and AWS credentials.

3. **Execute the Data Pipeline**: Connect to your cloud environment and run the scripts as you would locally:
   ```bash
   python crypto_bigquery_data_processing.py
   python crypto_localstack_s3_data_loader.py
   ```
   Or, use the executor script to run both sequentially:
   ```bash
   python crypto_datapipeline_executor.py
   ```

### Logging
All scripts use Python's built-in logging module to log information and errors. Logs include timestamps, log levels, and messages.