import boto3
from botocore.exceptions import ClientError
import os


AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')
boto3.setup_default_session(profile_name=AWS_PROFILE)

# Instantiating the Boto3 client
loaclstack_client = boto3.client("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

# Instantiating the Boto3 LocalStack resource

loaclstack_resource = boto3.resource("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

