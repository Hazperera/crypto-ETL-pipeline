import logging
from google.cloud import bigquery
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

def execute_query(query):
    """Executes a sample query."""
    client = bigquery.Client()
    try:
        query_job = client.query(query)
        return query_job.result()  # Waits for query to finish
    except Exception as e:
        logging.error(f'Error executing query: {e}')
        raise

def main():
    """Main function to execute the data pipeline."""
    try:
        # Perform a query
        monthly_active_addresses = '''
        WITH all_transactions AS (
            SELECT block_timestamp, amount FROM `public-data-finance.crypto_zilliqa.transactions`
            UNION ALL
            SELECT block_timestamp, amount FROM `public-data-finance.crypto_zilliqa.transitions`
        )
        SELECT DATE(block_timestamp) AS date, SUM(amount) / 1e12 AS volume
        FROM all_transactions
        GROUP BY date
        ORDER BY date DESC
        LIMIT 1000
        '''

        # Execute query
        rows = execute_query(monthly_active_addresses)

        # Convert query result to DataFrame
        df = pd.DataFrame([dict(row) for row in rows])

        # Write DataFrame to Parquet file
        df.to_parquet('crypto_zilliqa_transactions_new.parquet', index=False)

        # Log success message
        logging.info('Data written to Parquet file successfully.')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
