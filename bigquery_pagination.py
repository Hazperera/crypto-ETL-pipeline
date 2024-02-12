import logging
from google.cloud import bigquery
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_data_with_pagination(query, max_results=100):
    """Fetches data from BigQuery with pagination."""
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Execute the query
    query_job = client.query(query)

    # Initialize an empty DataFrame to store all fetched rows
    all_rows = pd.DataFrame()

    # Fetch results with pagination
    iterator = query_job.result(max_results=max_results)

    # Continuously fetch pages
    while True:
        # Convert rows to DataFrame
        try:
            page_df = iterator.to_dataframe()
        except StopIteration:
            break  # Exit loop if no more pages

        # Append current page to all_rows
        all_rows = pd.concat([all_rows, page_df])

        # Log progress
        logging.info(f'Processed {len(all_rows)} rows so far.')

        # Check if there are more pages
        if iterator.next_page_token is None:
            logging.info('All pages have been processed.')
            break  # Exit loop if no more pages
        else:
            iterator = client.query(query).result(page_token=iterator.next_page_token, max_results=max_results)

    return all_rows


def main():
    """Main function to execute the data pipeline."""
    try:
        # Perform queries
        monthly_active_addresses = '''
        SELECT 
            DATE(TIMESTAMP_TRUNC(block_timestamp, MONTH, "UTC")) AS month,
            COUNT(DISTINCT sender) AS active_addresses
        FROM `public-data-finance.crypto_zilliqa.transactions`
        GROUP BY month
        ORDER BY month DESC
        '''

        # Fetch data with pagination
        df = fetch_data_with_pagination(monthly_active_addresses)

        # Write DataFrame to Parquet file
        df.to_csv('crypto_zilliqa_transactions_new.csv', index=False)

        # Log success message
        logging.info('Data written to CSV file successfully.')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()