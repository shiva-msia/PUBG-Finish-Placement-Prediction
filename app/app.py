import pickle
import pandas as pd
import numpy as np
from flask import render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import boto3
import logging.config


logger = logging.getLogger(__name__)


# Initialize the Flask application
app = Flask(__name__)

# Configure flask app from config.py
app.config.from_object('app.app_config')

# Initialize the database
db = SQLAlchemy(app)


@app.route('/')
def index():
    """PUBG app page.

    Returns: rendered html template
    """
    try:
        return render_template('index.html')
    except:
        return render_template('error.html')


@app.route('/add', methods=['POST', 'GET'])
def add_entry():
    """View that process a POST with new customer input
    Returns: rendered html template with evaluation results.
    """

    try:
        boosts = request.form['Boosts']
        damageDealt = request.form['damageDealt']
        heals = request.form['heals']
        killStreaks = request.form['killStreaks']
        longestKill = request.form['longestKill']
        rideDistance = request.form['rideDistance']
        walkDistance = request.form['walkDistance']
        weaponsAcquired = request.form['weaponsAcquired']
        print("here")
        print("here")

        # load trained model
        model_path = app.config["MODEL_PATH"]
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        session = boto3.session.Session(region_name='us-east-1')
        s3client = session.client('s3')
        response = s3client.get_object(Bucket=app.config['S3_BUCKET'], Key=app.config["MODEL_PATH"])
        body = response['Body'].read()
        model = pickle.loads(body)
        logger.info("model loaded!")

        predicted = model.predict(pd.DataFrame({'boosts': boosts,
                                                'damageDealt': damageDealt,
                                                'heals': heals,
                                                'killStreaks': killStreaks,
                                                'longestKill': longestKill,
                                                'rideDistance': rideDistance,
                                                'walkDistance': walkDistance,
                                                'weaponsAcquired': weaponsAcquired
                                                }, index=[0]))

        predicted = np.where(predicted < 0, 0, predicted)
        predicted = np.where(predicted > 1, 1, predicted)
        place = ((1 - predicted.round(2)) * 100).astype('int')

        return render_template('index.html', result=place[0], confusion=app.config["CONFUSION_PATH"])
    except:
        return render_template('error.html')
