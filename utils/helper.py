import boto3

access_key = 'AKIA4NRIXPCI2ICIZZ7I'

secret_key = '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'

region = 'eu-west-1'

bucket_name = 'payyminnute'


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
