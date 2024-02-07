# from google.cloud import bigquery
# from google.cloud.exceptions import GoogleCloudError
# import logging

# client = bigquery.Client()


# def extract_transform():


# # summary of 

# daily_transaction_query = [
#     'CREATE TABLE datafella-workbook.dbt_hp.crypto_daily_transaction_summary AS'
#     'SELECT DATE(block_timestamp) as transaction_date,' 
#     'COUNT(id) as total_transactions,'
#     'SUM(amount) as total_amount'
#     'FROM `public-data-finance.crypto_zilliqa.transactions`'
#     'GROUP BY transaction_date'
# ]
    
# query_job = client.query(daily_transaction_query)  # API request
# rows = query_job.result()  # Waits for query to finish

# for row in rows:
#     print(row.name)


# def load_data_to_parquet(df, output_file):







