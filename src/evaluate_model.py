import pandas as pd
import numpy as np
import yaml
import pickle
import seaborn
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn import metrics
from io import BytesIO
import boto3


def eveluate_model(actual, predicted):
    """
            Predict finish place for the players in test data
            :param  actual: actual finish place
                    predicted: predicted finish place
            :return: r2: R-square of the value from the test data predictions
                     confusion_matrix:
    """
    r2 = r2_score(actual, predicted)

    temp_actual = np.where((actual > 0) & (actual <= 0.25), 2, actual)
    temp_actual = np.where((temp_actual > 0.25) & (temp_actual <= 0.5), 3, temp_actual)
    temp_actual = np.where((temp_actual > 0.5) & (temp_actual <= 0.75), 4, temp_actual)
    temp_actual = np.where((temp_actual > 0.75) & (temp_actual <= 1), 5, temp_actual)
    temp_predicted = np.where((predicted > 0) & (predicted <= 0.25), 2, predicted)
    temp_predicted = np.where((temp_predicted > 0.25) & (temp_predicted <= 0.5), 3, temp_predicted)
    temp_predicted = np.where((temp_predicted > 0.5) & (temp_predicted <= 0.75), 4, temp_predicted)
    temp_predicted = np.where((temp_predicted > 0.75) & (temp_predicted <= 1), 5, temp_predicted)
    confusion_matrix = metrics.confusion_matrix(temp_actual.astype("int"), temp_predicted.astype("int"),
                                                labels=[2, 3, 4, 5])
    return r2, confusion_matrix


def plot_confusion(confusion_data, save_path):
    """Plot confusion matrix by dividing PUBG players into quartiles"""
    seaborn.set_style("whitegrid", {'axes.grid' : False})
    seaborn.heatmap(confusion_data, annot=confusion_data, fmt='0.0f', cmap='Wistia')
    plt.xlabel('Actual'), plt.ylabel('Predicted'), plt.title('Confusion matrix')
    plt.savefig(save_path)
    plt.close()
    s3 = boto3.client('s3')
    s3 = boto3.client('s3')
    bucket = 'pubg-finish-prediction-app'
    file_name = save_path
    key_name = save_path
    s3.upload_file(file_name, bucket, key_name)


def plot_feature_importance(model, predictor, save_path):
    """Plot feature importance from Random Forest model"""
    features = predictor.columns
    importances = model.feature_importances_
    indices = np.argsort(importances)
    plt.title('Feature Importance')
    plt.barh(range(len(indices)), importances[indices], align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.savefig(save_path)
    plt.close()
    s3 = boto3.client('s3')
    bucket = 'pubg-finish-prediction-app'
    file_name = save_path
    key_name = save_path
    s3.upload_file(file_name, bucket, key_name)


def run_evaluate(args):
    with open(args.config, "r") as f:
        config = yaml.load(f)

    test_response = pd.read_csv("https://pubg-finish-prediction-app.s3.us-east-2.amazonaws.com/" + config['evaluate']['RESPONSE'])
    client = boto3.client('s3')  # low-level functional API
    obj = client.get_object(Bucket='pubg-finish-prediction-app', Key=config['evaluate']['PREDICTED'])
    predicted = np.load(BytesIO(obj['Body'].read()))
    r2, confusion_mat = eveluate_model(test_response, predicted)

    confusion_path = config['evaluate']['CONFUSION_PATH']
    plot_confusion(confusion_mat, confusion_path)

    importance_path = config['evaluate']['IMPORTANCE_PATH']
    session = boto3.session.Session(region_name='us-east-1')
    s3client = session.client('s3')
    response = s3client.get_object(Bucket=config['evaluate']['S3_BUCKET'], Key=config['evaluate']['MODEL_PATH'])
    body = response['Body'].read()
    rf_fit = pickle.loads(body)
    train_predictor = pd.read_csv("https://pubg-finish-prediction-app.s3.us-east-2.amazonaws.com/" + config['evaluate']['PREDICTOR'])
    plot_feature_importance(rf_fit, train_predictor, importance_path)
    s3_resource = boto3.resource('s3')
    np.save(open(config['evaluate']['R2_PATH'], "wb"), predicted)
    s3_resource.Object(config['evaluate']['S3_BUCKET'], config['evaluate']['R2_PATH']).put(Body=open(config['evaluate']['R2_PATH'], 'rb'))

