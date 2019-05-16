"""This module can be used to upload PUBG train and test data to the your desired S3 bucket

To write PUBG data in your local:
    Step 1: Change the S3 bucket name in the bottom of the code to desired bucket name
    Step 2: Run in cmd - `python write_to_s3.py`
"""


import boto3

s3 = boto3.client('s3')


def write_to_s3(bucket_name='pubg-finish-prediction-app'):
    """
        Write PUBG data to the desired S3 bucket
        :param bucket_name: The S3 bucket in which the csv will be stored
        :return: None
    """

    copy_source = {'Bucket': 'pubg-finish-prediction-app',
                   'Key': 'Data/train_pubg.csv'}
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.copy(copy_source, 'train_pubg.csv')

    copy_source = {'Bucket': 'pubg-finish-prediction-app',
                   'Key': 'Data/test_pubg.csv'}
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.copy(copy_source, 'test_pubg.csv')


write_to_s3(bucket_name='pubg-finish-prediction-app')