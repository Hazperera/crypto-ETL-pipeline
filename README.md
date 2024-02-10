Setup and Run Data Pipeline:
Environment Setup:

Make sure you have Python 3.12 installed on your system.
Set up a virtual environment for the project to manage dependencies.
Install Poetry, a dependency management tool, using the following command:
bash
Copy code
pip install poetry
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install Dependencies:

Run the following command to install project dependencies:
bash
Copy code
poetry install
Run the Data Pipeline:

Execute the main Python script to run the data pipeline:
bash
Copy code
poetry run python bq_to_parquet.py
Code Comments:
python
Copy code
import logging
from google.cloud import bigquery
import pandas as pd

def execute_query(query):
    """Executes a BigQuery query."""
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
        # Perform a query to retrieve monthly active addresses
        monthly_active_addresses_query = '''
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

        # Execute the query
        rows = execute_query(monthly_active_addresses_query)

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
System Architecture Diagram:

Components:
Data Pipeline: A Python script (bq_to_parquet.py) that queries data from BigQuery, processes it, and stores it in Parquet format.
Google Cloud Platform (GCP): Used to host BigQuery, where the data resides.
Poetry: Manages project dependencies.
Logging: Logs are generated to track pipeline execution and any errors encountered.
System Scalability and Edge Cases:
Scalability:

BigQuery is highly scalable and can handle large datasets efficiently.
The pipeline can be scaled horizontally by running multiple instances of the data pipeline script to process data in parallel.
Autoscaling can be configured for GCP resources to handle variable workloads.
Edge Cases:

Ensure proper error handling to handle potential issues such as network errors, query failures, and data inconsistencies.
Implement retry mechanisms for transient errors.
Monitor resource usage and performance metrics to detect and mitigate any issues in real-time.
Additional Considerations:
Security: Ensure proper access controls and encryption mechanisms are in place to protect sensitive data.
Cost Optimization: Monitor resource usage and optimize configurations to minimize costs, especially for BigQuery usage.
Data Quality: Implement data validation checks to ensure data integrity and accuracy.
Continuous Integration/Continuous Deployment (CI/CD): Set up automated testing and deployment pipelines to streamline development and deployment processes.
By following these guidelines, you can effectively set up and run the data pipeline, handle edge cases, and design a scalable architecture for production use.



