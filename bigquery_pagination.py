import logging
from google.cloud import bigquery
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_data_with_pagination(query, max_results=100):
    """Fetches data from BigQuery with pagination."""
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Initialize an empty DataFrame to store all fetched rows
    all_rows = pd.DataFrame()

    # Execute the query
    query_job = client.query(query)

    # Fetch results with pagination
    iterator = query_job.result(page_size=max_results)
    page = iterator.page

    # Continuously fetch pages
    while page is not None:
        # Convert the current page into a DataFrame
        page_df = page.to_dataframe()

        # Append current page to all_rows
        all_rows = pd.concat([all_rows, page_df])

        # Log progress
        logging.info(f'Processed {len(page_df)} rows so far.')

        try:
            # Fetch next page
            page = next(iterator.pages)
        except StopIteration:
            # Exit loop if no more pages
            logging.info('All pages have been processed.')
            break

    return all_rows

# Rest of your main function remains the same


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
        df.to_parquet('crypto_zilliqa_transactions_new.parquet', index=False)

        # Log success message
        logging.info('Data written to Parquet file successfully.')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()