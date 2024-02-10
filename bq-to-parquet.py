from google.cloud import bigquery
import pandas as pd

# Initialize BigQuery client
client = bigquery.Client()

# Perform a query
monthly_active_addresses = '('
'WITH all_transactions AS'
'('
'SELECT block_timestamp, amount'
'FROM `public-data-finance.crypto_zilliqa.transactions`'
'UNION ALL'
'SELECT block_timestamp, amount'
'FROM `public-data-finance.crypto_zilliqa.transitions`'
')'
'SELECT DATE(block_timestamp) AS date,'
'SUM(amount) / 1e12 AS volume'
'FROM all_transactions'
'GROUP BY date'
'ORDER BY date DESC'
'LIMIT 1000'

query_job = client.query(monthly_active_addresses)  # API request
rows = query_job.result()  # Waits for query to finish

# Convert query result to DataFrame
df = pd.DataFrame([dict(row) for row in rows])

# Write DataFrame to Parquet file
df.to_parquet('crypto_zilliqa_transactions_new.parquet', index=False)






