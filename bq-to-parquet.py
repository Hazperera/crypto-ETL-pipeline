from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Perform a query
QUERY = (
    'SELECT * FROM `public-data-finance.crypto_zilliqa.transactions` '
    'LIMIT 10')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row)






