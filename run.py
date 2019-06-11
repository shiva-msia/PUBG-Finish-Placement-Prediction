import argparse

from src.create_database_rds import create_db
from src.generate_features import run_generate
from src.train_model import run_train
from src.score_model import run_score
from src.evaluate_model import run_evaluate
from app.app import app
import logging.config

logging.config.fileConfig("config/logging/local.conf")
logger = logging.getLogger("pubg_predictor")


def run_app():
    """Function to run flask app"""
    # Configure flask app from config.py
    app.config.from_object('app.app_config')
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run components of the model source code")
    subparsers = parser.add_subparsers()

    # DATABASE subparser
    sb_db = subparsers.add_parser("create_db", description="Create Database")
    sb_db.add_argument('--user', default=None, help="Username for connecting to the database")
    sb_db.add_argument('--password', default=None, help='Password')
    sb_db.set_defaults(func=create_db)

    # FEATURE subparser
    sb_features = subparsers.add_parser("generate_features", description="Generate features")
    sb_features.add_argument('--config', default='config/config.yml', help='path to yaml file with configurations')
    sb_features.add_argument('--user', default=None, help="Username for connecting to the database")
    sb_features.add_argument('--password', default=None, help='Password')
    sb_features.add_argument('--input', default=None, help="Path to CSV for input to model scoring")
    sb_features.add_argument('--output', default=None, help='Path to where the data set should be saved to (optional)')
    sb_features.set_defaults(func=run_generate)

    # TRAIN subparser
    sb_train = subparsers.add_parser("train_model", description="Train model")
    sb_train.add_argument('--config', default='config/config.yml', help='path to yaml file with configurations')
    sb_train.add_argument('--input', default=None, help="Path to CSV for input to model training")
    sb_train.add_argument('--output', default=None, help='Path to where the dataset should be saved to (optional')
    sb_train.set_defaults(func=run_train)

    # SCORE subparser
    sb_score = subparsers.add_parser("score_model", description="Score model")
    sb_score.add_argument('--config', default='config/config.yml', help='path to yaml file with configurations')
    sb_score.add_argument('--input', default=None, help="Path to CSV for input to model scoring")
    sb_score.add_argument('--output', default=None, help='Path to where the dataset should be saved to (optional')
    sb_score.set_defaults(func=run_score)

    # EVALUATION subparser
    sb_eval = subparsers.add_parser("evaluate_model", description="Evaluate model")
    sb_eval.add_argument('--config', default='config/config.yml', help='path to yaml file with configurations')
    sb_eval.add_argument('--input', default=None, help="Path to CSV for input to model evaluation")
    sb_eval.add_argument('--output', default=None, help='Path to where the dataset should be saved to (optional')
    sb_eval.set_defaults(func=run_evaluate)

    # RUN APP subparser
    sb_run = subparsers.add_parser("app", description="Run Flask app")
    sb_run.set_defaults(func=run_app)

    args = parser.parse_args()
    args.func(args)
