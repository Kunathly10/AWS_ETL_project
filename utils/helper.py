import boto3
from configparser import ConfigParser
config = ConfigParser()
region = config['AWS']['region']
bucket_name =config['AWS']['bucket_name']
access_key = config['AWS']['access_key']
secret_key = config['AWS']['secret_key']


def create_bucket():
    client = boto3.client(
        's3',
        aws_access_key_id= access_key,
        aws_secret_access_key=secret_key
        
    )

    client.create_bucket(
        Bucket= bucket_name,

        CreateBucketConfiguration = {

            "LocationConstraint": region
            
        }
    )
