import pickle
# import traceback
# import os
# import xgboost
import pandas as pd
import numpy as np
from flask import render_template, request, redirect, url_for
# from app import db, app
from flask import Flask
# from src.models import Churn_Prediction
from flask_sqlalchemy import SQLAlchemy
import boto3

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
        # logger.info("model loaded!")

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

        # customer1 = Churn_Prediction(age=float(Age), activeMember=float(IsActiveMember),
        #                              numProducts=float(NumOfProducts),
        #                              fromGermany=float(Germany), gender=float(Male), balance=float(Balance),
        #                              hasCrCard=float(HasCrCard),
        #                              tenure=float(Tenure), predicted_score=float(prob))
        # db.session.add(customer1)
        # db.session.commit()

        # logger.info("New customer evaluated as: %s", evaluation)

        # result = "This customer will churn with probability {:0.3f} - classified as {}".format(prob, evaluation)
        # return redirect(url_for('index'))
        print('here')
        print(place)
        print('here')
        # return render_template('index.html', result=result)
        return render_template('index.html', result=place[0], confusion=app.config["CONFUSION_PATH"])
    except:
        # traceback.print_exc()
        # logger.warning("Not able to display evaluations, error page returned")
        return render_template('error.html')


# if __name__ == "__main__":
#     app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])
