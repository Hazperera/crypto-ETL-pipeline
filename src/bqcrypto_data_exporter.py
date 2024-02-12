import os
import logging
from google.cloud import bigquery
import pandas as pd
from importlib import import_module

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
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    output_dir = os.path.join(parent_dir, 'output')
    output_path = os.path.join(output_dir, filename)

    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        df = fetch_data_with_pagination(query)
        df.to_parquet(output_path, index=False)
        logging.info(f'Data written to {output_path} successfully.')
    except Exception as e:
        logging.error(f'An error occurred while processing {output_path}: {e}')

def main():
    """Main function to execute the data pipeline."""
    try:
        # Dynamically import queries module
        queries_module = import_module('queries')

        # Get all variables/functions from the queries module
        query_names = [name for name in dir(queries_module) if not name.startswith('__')]

        # Process queries and write to files
        for query_name in query_names:
            query = getattr(queries_module, query_name)
            filename = query_name.lower() + '.parquet'
            query_and_write_to_file(query, filename)

        logging.info('All data written to files successfully.')

    except Exception as e:
        logging.error(f'An error occurred in main: {e}')

if __name__ == "__main__":
    main()
