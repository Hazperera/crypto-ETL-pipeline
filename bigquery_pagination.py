import logging
from google.cloud import bigquery
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_data_with_pagination(query, max_results=100):
    """Fetches data from BigQuery with pagination."""
    # Construct a BigQuery client object.
    client = bigquery.Client()
    page_token = None
    all_rows = []

    # Continuously fetch pages
    while True:
        rows_iter = client.query(query, max_results=max_results, page_token=page_token)
        rows = list(rows_iter)
        all_rows.extend(rows)

        # Log progress
        logging.info(f'Processed {len(all_rows)} rows so far.')

        page_token = rows_iter.next_page_token
        if not page_token:
            logging.info('All pages have been processed.')
            break  # Exit loop if no more pages

    return all_rows

def main():
    """Main function to execute the data pipeline."""
    try:
        # Perform queries
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

        # Fetch data with pagination
        rows = fetch_data_with_pagination(monthly_active_addresses)

        # Convert query result to DataFrame
        df = pd.DataFrame([dict(row) for row in rows])

        # Write DataFrame to Parquet file
        df.to_parquet('crypto_zilliqa_transactions123.parquet', index=False)

        # Log success message
        logging.info('Data written to Parquet file successfully.')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
