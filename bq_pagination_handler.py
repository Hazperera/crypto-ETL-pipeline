import logging
from google.cloud import bigquery
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    """Main function to execute the data pipeline."""
    try:
        # Construct a BigQuery client object.
        client = bigquery.Client()
        table_id = "public-data-finance.crypto_zilliqa.transactions"

        # Initialize variables for pagination
        max_results = 20  # Set the number of rows to fetch per page
        page_token = None
        all_rows = []

        # Continuously fetch pages
        while True:
            rows_iter = client.list_rows(table_id, max_results=max_results, page_token=page_token)
            rows = list(rows_iter)
            all_rows.extend(rows)
            page_token = rows_iter.next_page_token
            if not page_token:
                break  # Exit loop if no more pages

        # Convert rows to DataFrame
        df = pd.DataFrame([dict(row) for row in rows])

        # Write DataFrame to Parquet file
        df.to_csv('crypto_zilliqa_pagination_transactions.csv', index=False)

        # Log success message
        logging.info(f'Data written to Parquet file successfully. Total rows: {len(rows)}')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
