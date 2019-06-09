from os import path

# Getting the parent directory of this file. That will function as the project home.
PROJECT_HOME = path.dirname(path.abspath(__file__))

# DBCONFIG specifies the yaml file with settings for creation of RDS database
DBCONFIG = path.join(PROJECT_HOME, '../config/dbconfig.yml')

DEBUG = True
PORT = 3000
APP_NAME = "PUBG"

# The SQLALCHEMY_DATABASE_URI parameter is considered ONLY if DBCONFIG is set as None. Else it is ignored.
DB_PATH = path.join(PROJECT_HOME, 'PUBG.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = True
HOST = "127.0.0.1"

S3_BUCKET = 'pubg-finish-prediction-app'
MODEL_PATH = 'models/random_forest_model.pkl'
CONFUSION_PATH = 'figures/confusion_matrix.jpeg'
IMPORTANCE_PATH = 'figures/feature_importance.jpeg'
