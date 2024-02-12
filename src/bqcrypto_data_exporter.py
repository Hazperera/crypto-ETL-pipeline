import logging
from google.cloud import bigquery
import pandas as pd
from queries import *

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_data_with_pagination(query, max_results=None):
    """Fetches data from BigQuery with pagination."""
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Execute the query
    query_job = client.query(query)

    # Fetch results and convert to DataFrame
    iterator = query_job.result()
    all_rows = iterator.to_dataframe()

    # If max_results is set, truncate the DataFrame
    if max_results is not None:
        all_rows = all_rows.head(max_results)

    return all_rows


def query_and_write_to_file(query, filename):
    """Fetches data using the provided query and writes it to a file."""
    # Manually construct the output path
    output_path = 'output/' + filename  
    
    try:
        df = fetch_data_with_pagination(query)
        df.to_csv(output_path, index=False)
        logging.info(f'Data written to {output_path} successfully.')
    except Exception as e:
        logging.error(f'An error occurred while processing {output_path}: {e}')


def main():
    """Main function to execute the data pipeline."""
    try:
        # Process queries and write to files
        query_and_write_to_file(MONTHLY_ACTIVE_ADDRESSES, 'monthly_active_addresses.csv')
        query_and_write_to_file(DAILY_TRANSACTION_VOLUME, 'daily_transaction_volume.csv')


        logging.info('All data written to files successfully.')

    except Exception as e:
        logging.error(f'An error occurred in main: {e}')

if __name__ == "__main__":
    main()
