import logging
import os
from crypto_bigquery_data_processing import main as crypto_bigquery_data_processing_main
from crypto_localstack_s3_data_loader import main as crypto_localstack_s3_data_loader_main

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    """Orchestrates the execution of the two separate scripts."""
    try:
        # Execute script 1 (AWS S3 operations)
        logging.info('Executing crypto_bigquery_data_processing.py...')
        crypto_bigquery_data_processing_main()

        # Execute script 2 (Google BigQuery operations)
        logging.info('Executing crypto_localstack_s3_data_loader.py...')
        crypto_localstack_s3_data_loader_main()

        logging.info('All scripts executed successfully.')

    except Exception as e:
        logging.error(f'An error occurred in main: {e}')

if __name__ == "__main__":
    main()
