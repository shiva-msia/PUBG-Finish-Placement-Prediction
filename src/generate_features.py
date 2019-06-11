import yaml
import pandas as pd
import boto3
from io import StringIO
from sklearn.model_selection import train_test_split
import pymysql
import src.config
import logging.config


logger = logging.getLogger(__name__)


def acquire_data(user, password):
    """
        Import PUBG data from S3 bucket
        :param data_path: S3 bucket path to PUBG data
        :return: data: pandas data frame of PUBG data
    """
    with open(src.config.DBCONFIG, "r") as f:
        db = yaml.load(f)
    conn = pymysql.connect(host=db['host'], user=user, port=db['port'], passwd=password, db=db['dbname'])
    data = pd.read_sql('select * from train_pubg;', con=conn)
    logger.info("Data acquired from RDS")
    return data


def generate_features(data, feature_list):
    """
                Import PUBG data from S3 bucket
                :param data: pandas data frame of PUBG data
                :return: X_train: train data predictors data frame
                         X_test: test data predictors data frame
                         y_train: train data response data frame
                         y_test: test data response data frame
    """

    # short = data[data['matchType'] == 'solo']
    features = data[feature_list]
    clean = features.round(2)
    response = clean['winPlacePerc']
    predictor = clean.drop(['winPlacePerc'],axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(predictor, response, test_size=0.3)
    logger.info("Generated Features")
    return X_train, X_test, y_train, y_test


def save_data(data, s3_bucket, save_path):
    """ write full data to csv that will be used going forward
        :param data: send in the df to save
        :param s3_bucket: name of s3 bucket to save data
        :param save_path:  send in the path name to store the file
    """
    csv_buffer = StringIO()
    data.to_csv(csv_buffer, header=True, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(s3_bucket, save_path).put(Body=csv_buffer.getvalue())
    logger.info("Features saved in S3")


def run_generate(args):
    with open(args.config, "r") as f:
        config = yaml.load(f)
    pubg_df = acquire_data(user=args.user, password=args.password)
    features = config['generate_features']['FEATURES']
    train_predictor, test_predictor, train_response, test_response = generate_features(pubg_df, features)
    save_data(train_predictor, config['generate_features']['S3_BUCKET'], config['generate_features']['TRAIN_X_PATH'])
    save_data(test_predictor, config['generate_features']['S3_BUCKET'], config['generate_features']['TEST_X_PATH'])
    save_data(train_response, config['generate_features']['S3_BUCKET'], config['generate_features']['TRAIN_Y_PATH'])
    save_data(test_response, config['generate_features']['S3_BUCKET'], config['generate_features']['TEST_Y_PATH'])
