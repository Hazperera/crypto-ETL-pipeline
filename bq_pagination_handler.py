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

        # TODO: Replace with your table ID
        table_id = "your-project.your_dataset.your_table_name"

        # Use client.list_rows for pagination
        # Fetch rows with a limit
        max_results = 1000  # Set the number of rows to fetch per page
        rows_iter = client.list_rows(table_id, max_results=max_results)
        rows = list(rows_iter)

        # Convert rows to DataFrame
        df = pd.DataFrame([dict(row) for row in rows])

        # Write DataFrame to Parquet file
        df.to_parquet('output_filename.parquet', index=False)

        # Log success message
        logging.info(f'Data written to Parquet file successfully. Total rows: {len(rows)}')

    except Exception as e:
        # Log error message
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
