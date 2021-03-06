import numpy as np
import sys
import os
import yaml
import boto3
from io import BytesIO
sys.path.append(os.path.join('../../'))


def test_evaluate_model():
    config = yaml.load(open("../../config/config.yml", "r"))
    client = boto3.client('s3')  # low-level functional API
    obj = client.get_object(Bucket='pubg-finish-prediction-app', Key=config['evaluate']['R2_PATH'])
    r2 = np.load(BytesIO(obj['Body'].read()))
    assert r2 > 0.70

