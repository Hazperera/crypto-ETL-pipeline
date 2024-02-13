import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

AWS_REGION = 'eu-west-1'
AWS_PROFILE = 'hasa-dev'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
ENDPOINT_URL = None
# ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')
# print("Endpoint URL:", ENDPOINT_URL)

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)

# S3 bucket name
BUCKET_NAME = 'hasa-dev-218084585641'

# Initialize S3 client
s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_REGION,endpoint_url=ENDPOINT_URL)

# def create_bucket(bucket_name, region_name=None):
#     """
#     Creates an S3 bucket.
#     """
#     try:
#         if region_name is None or region_name == 'us-east-1':
#             response = s3_client.create_bucket(Bucket=bucket_name)
#         else:
#             response = s3_client.create_bucket(
#                 Bucket=bucket_name,
#                 CreateBucketConfiguration={'LocationConstraint': region_name})
#     except ClientError:
#         logger.exception('Could not create S3 bucket locally.')
#         raise
#     else:
#         return response

def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to a S3 bucket.
    """
    try:
        if object_name is None:
            object_name = os.path.basename(file_name)
        response = s3_client.upload_file(
            file_name, bucket, object_name)
    except ClientError:
        logger.exception('Could not upload file to S3 bucket.')
        raise
    else:
        return response
    
def list_files(bucket):
    """
    List files in an S3 bucket.
    """
    files = []
    try:
        response = s3_client.list_objects_v2(Bucket=bucket)
        for item in response.get('Contents', []):
            files.append(item['Key'])
    except ClientError as e:
        logging.error(e)
        return None
    return files

    
def main():
    """
    Main invocation function.
    """
    bucket_name = BUCKET_NAME
    output_folder = "/Users/hasaniperera/crypto-ETL-pipeline/output"  

    # logger.info('Creating S3 bucket locally using LocalStack...')
    # s3 = create_bucket(bucket_name)
    # logger.info('S3 bucket created.')    
    # logger.info(json.dumps(s3, indent=4) + '\n')

# Iterate through each file in the output folder
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            logger.info(f'Uploading file {file_path} to S3 bucket...')
            upload_response = upload_file(file_path, bucket_name)
            logger.info('File uploaded.')

# List files in the bucket
    logger.info('Listing files in S3 bucket...')
    files = list_files(bucket_name)
    for file in files:
        print(file)


if __name__ == '__main__':
    main()
