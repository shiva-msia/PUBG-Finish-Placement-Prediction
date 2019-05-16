"""This module combines argparsing for the create_database_rds module and enables the execution of the same scripts

To create a database in RDS:
    Run in cmd - `python run_create_database_rds.py --user <username> --password <password>`
"""

import argparse
from create_database_rds import create_db

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run components of the model source code")
    parser.add_argument("--user", default="", help="Username for connecting to the database")
    parser.add_argument("--password", default="", help="Password")
    parser.set_defaults(func=create_db)
    args = parser.parse_args()
    args.func(args)