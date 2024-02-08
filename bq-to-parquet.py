from google.cloud import bigquery
import pandas as pd

# Initialize BigQuery client
client = bigquery.Client()

# Perform a query
first_query = (
    'SELECT * '
    'FROM `public-data-finance.crypto_zilliqa.transactions` '
    'LIMIT 1')
query_job = client.query(first_query)  # API request
rows = query_job.result()  # Waits for query to finish

# Convert query result to DataFrame
df = pd.DataFrame([dict(row) for row in rows])

# Write DataFrame to Parquet file
df.to_parquet('crypto_zilliqa_transactions.parquet', index=False)






