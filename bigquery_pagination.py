import logging
from google.cloud import bigquery
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_data_with_pagination(query, max_results=100):
    """Fetches data from BigQuery with pagination."""
    # Construct a BigQuery client object.
    client = bigquery.Client()
    # Initialize variables for pagination
    page_token = None
    # Initialize an empty list to store all fetched rows
    all_rows = []

    # Continuously fetch pages
    while True:
        # Execute query and fetch next page of results
        job_config = bigquery.QueryJobConfig(max_results=max_results, page_token=page_token)
        query_job = client.query(query, job_config=job_config)
        page_rows = query_job.to_dataframe()

        # Append fetched rows to all_rows
        all_rows.append(page_rows)

        # Log progress
        logging.info(f'Processed {len(all_rows)} pages so far.')

        # Check if there are more pages
        if query_job.next_page_token is None:
            logging.info('All pages have been processed.')
            break  # Exit loop if no more pages
        else:
            page_token = query_job.next_page_token

    # Concatenate all rows into a single DataFrame
    return pd.concat(all_rows)

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
        df = fetch_data_with_pagination(monthly_active_addresses)

        # Write DataFrame to Parquet file
        df.to_parquet('crypto_zilliqa_transactions123.parquet', index=False)

        # Log success message
        logging.info('Data written to Parquet file successfully.')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()