import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')
# print("Endpoint URL:", ENDPOINT_URL)

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)
# s3_client = boto3.client("s3", region_name=AWS_REGION,
#                          endpoint_url=ENDPOINT_URL)

######## Hardcoded Credentials (Temporary Test) ########
s3_client = boto3.client('s3', region_name=AWS_REGION, 
                         endpoint_url=ENDPOINT_URL, 
                         aws_access_key_id='test', 
                         aws_secret_access_key='test')


def create_bucket(bucket_name):
    """
    Creates a S3 bucket.
    """
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': AWS_REGION})
    except ClientError:
        logger.exception('Could not create S3 bucket locally.')
        raise
    else:
        return response

def main():
    """
    Main invocation function.
    """
    bucket_name = "hands-on-cloud-localstack-bucket"
    logger.info('Creating S3 bucket locally using LocalStack...')
    s3 = create_bucket(bucket_name)
    logger.info('S3 bucket created.')
    logger.info(json.dumps(s3, indent=4) + '\n')

if __name__ == '__main__':
    main()
