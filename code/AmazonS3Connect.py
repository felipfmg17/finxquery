import boto3
import os

AWS_REGION = 'us-east-2'
AWS_USER_KEY_FILE_NAME = '~/local_finx_query/aws_user_key.txt'

file_path = os.path.expanduser(AWS_USER_KEY_FILE_NAME)
with open(file_path, 'r') as file:
  ACCESS_KEY = file.readline().strip()
  PRIVATE_KEY = file.readline().strip()


s3 = boto3.client(
    service_name = 's3',
    region_name = AWS_REGION,
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = PRIVATE_KEY
  )
s3.upload_file('../files/ibm_balance.txt', 'raw-dev-finxquery', 'test/files/ibm_balance_3.txt')



