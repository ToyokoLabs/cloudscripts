"""
List all files in a AWS bucket.

There should be a credentials file in ~/.aws/credentials with this content:

[default]
aws_access_key_id = XXXXX
aws_secret_access_key = XXXXXXXXXXX
region = us-west-1
"""

import boto3

# Bucket name
BN = '' 

s3client = boto3.client('s3')
los = s3client.list_objects_v2(Bucket=BN)
for lo in los['Contents']:
    print(lo['Key'])
