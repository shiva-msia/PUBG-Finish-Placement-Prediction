import pandas as pd
import pickle
import yaml
import boto3
from sklearn.ensemble import RandomForestRegressor
import logging.config


logger = logging.getLogger(__name__)


def train_model(predictor, response):
    """
        Train Random Forest model on PUBG data
        :param  predictor: pandas data frame of model predictors
                response: pandas data frame of model response
        :return: fit: trained random forest model
    """

    rf = RandomForestRegressor(max_depth=5, n_estimators=300,random_state=False, verbose=False)
    fit = rf.fit(predictor, response)
    logger.info("Random Forest model trained")
    return fit


def save_model(model, s3_bucket, save_path):
    """ write full data to csv that will be used going forward
        :param data: send in the df to save
        :param s3_bucket: name of s3 bucket to save data
        :param save_path:  send in the path name to store the file
    """
    s3_resource = boto3.resource('s3')
    pickle.dump(model, open(save_path, "wb"))
    s3_resource.Object(s3_bucket, save_path).put(Body=open(save_path, 'rb'))
    logger.info("Random Forest model saved in S3")


def run_train(args):
    """Function to run train_model and save_model functions"""
    with open(args.config, "r") as f:
        config = yaml.load(f)
    train_predictor = pd.read_csv("https://pubg-finish-prediction-app.s3.us-east-2.amazonaws.com/" + config['train']['PREDICTOR'])
    train_response = pd.read_csv("https://pubg-finish-prediction-app.s3.us-east-2.amazonaws.com/" + config['train']['RESPONSE'])
    rf_fit = train_model(train_predictor, train_response)
    save_model(model=rf_fit, s3_bucket=config['train']['S3_BUCKET'], save_path=config['train']['MODEL_PATH'])
