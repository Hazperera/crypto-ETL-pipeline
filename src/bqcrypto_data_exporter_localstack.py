# import boto3
# import pandas as pd

# # Set up LocalStack S3 client
# s3 = boto3.client('s3', endpoint_url='http://localhost:4566')

# # Create a LocalStack S3 bucket
# bucket_name = 'my-local-bucket'
# s3.create_bucket(Bucket=bucket_name)

# # Convert data to Parquet format (example)
# data = {'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']}
# df = pd.DataFrame(data)
# parquet_file = 'data.parquet'
# df.to_parquet(parquet_file)

# # Upload Parquet file to LocalStack S3 bucket
# s3.upload_file(Filename=parquet_file, Bucket=bucket_name, Key='data.parquet')

# print("Parquet file uploaded to S3 bucket in LocalStack.")
