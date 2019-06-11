import numpy as np
import pandas as pd
import yaml
import pickle
import boto3
import logging.config


logger = logging.getLogger(__name__)


def score_model(model, data):
    """
        Predict finish place for the players in test data
        :param  model: trained random forest model
                data: pandas data frame of data to be predicted on
        :return: predicted: pandas data frame of predicted finish place
    """

    predicted = model.predict(data)
    predicted = np.where(predicted < 0, 0, predicted)
    predicted = np.where(predicted > 1, 1, predicted)
    logger.info("Model scored")
    return predicted


def run_score(args):
    """Function to run predict_model function"""
    with open(args.config, "r") as f:
        config = yaml.load(f)
    test_predictor = pd.read_csv("https://pubg-finish-prediction-app.s3.us-east-2.amazonaws.com/" + config['score']['PREDICTOR'])
    session = boto3.session.Session(region_name='us-east-1')
    s3client = session.client('s3')
    response = s3client.get_object(Bucket=config['score']['S3_BUCKET'], Key=config['score']['MODEL_PATH'])
    body = response['Body'].read()
    rf_fit = pickle.loads(body)
    predicted = score_model(rf_fit, test_predictor)
    s3_resource = boto3.resource('s3')
    np.save(open(config['score']['PREDICTED'], "wb"), predicted)
    s3_resource.Object(config['score']['S3_BUCKET'], config['score']['PREDICTED']).put(Body=open(config['score']['PREDICTED'], 'rb'))
