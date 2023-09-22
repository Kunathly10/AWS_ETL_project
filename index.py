import pandas as pd

from sqlalchemy import create_engine

import psycopg2

from configparser import ConfigParser
config = ConfigParser()
config.read('.env')


region = config['AWS']['region']
bucket_name =config['AWS']['bucket_name']
access_key = config['AWS']['access_key']
secret_key = config['AWS']['secret_key']

host = config['DB_CRED']['host']
database=  config['DB_CRED']['database']
user = config['DB_CRED']['user']
password = config['DB_CRED'] ['password']

# Step 1: Create an S3 bucket using boto3
from utils.helper import create_bucket
create_bucket()

# Step 2: Extract from database (postgresql) to data lake (S3)
conn = create_engine('postgresql+psycopg2://{user}:{password}*@localhost:5432/{database}')
from utils.constant import db_tables
s3_path = 's3://{}/{}.csv'

for table in db_tables:
    query = f'SELECT * FROM {table}'
    df = pd.read_sql_query(query, conn)
    s3_key = f"{table}.csv"
    
    #Loading to the s3 bucket datalake
    df.to_csv(
        s3_path.format(bucket_name, s3_key),
        index=False,
        storage_options={
            "key": access_key,
            "secret": secret_key
        }
    )
