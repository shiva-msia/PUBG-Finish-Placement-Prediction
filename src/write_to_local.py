"""This module can be used to write PUBG train and test data to the your directory

To write PUBG data in your local:
    Run in cmd - `python write_to_local.py`
"""


import boto3

s3 = boto3.client('s3')


def write_to_local():
    """
        Download PUBG data to the working directory from S3
        :return: None
    """

    s3.download_file('pubg-finish-prediction-app', 'Data/train_pubg.csv', 'train_pubg.csv')
    s3.download_file('pubg-finish-prediction-app', 'Data/test_pubg.csv', 'test_pubg.csv')


write_to_local()
