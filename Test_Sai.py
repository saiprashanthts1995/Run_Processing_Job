import boto3
import pandas as pd
from io import StringIO
import datetime
import os

def create_s3_client():
    # Initialize the S3 client
    s3 = boto3.client('s3')
    return s3

def create_sample_data():
    df = pd.DataFrame(data=[[1,2,3], [4,5,6], [7,8,9]], columns = ['a', 'b', 'c'])
    print(df.head())
    return df

def upload_data_to_csv(s3_client, file_key, df, bucket_name):
    # Convert DataFrame to CSV format
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    
    # Upload the DataFrame as a CSV file to S3
    s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=file_key)

    print(f"DataFrame saved as CSV to S3 bucket: {bucket_name}/{file_key}")

def main():
    BUCKET_NAME = 'docker-testing-s3-006'
    var1 = os.getenv('bucket')
    s3_client = create_s3_client()
    df = create_sample_data()
    now = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    file_key = f'saib_files/{var1}/a_{now}.csv'
    upload_data_to_csv(s3_client, file_key, df, BUCKET_NAME)

main()

