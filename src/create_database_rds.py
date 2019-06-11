"""This module contains functions to create a database in rds

To create a database in RDS run the module run_create_database_rds.py:
    Run in cmd - `python run_create_database_rds.py --user <username> --password <password>`
"""

import sys
import yaml
import sqlalchemy
import src.config
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import pymysql
import logging.config


logger = logging.getLogger(__name__)


def ifin(param, dictionary, alt=None):
    assert type(dictionary) == dict
    if param in dictionary:
        return dictionary[param]
    else:
        return alt


def create_connection(host='127.0.0.1', database="", sqltype="", port=10000,
                      username=None, password=None, dbconfig=None, engine_string=None):
    if engine_string is None:
        if dbconfig is not None:
            with open(dbconfig, "r") as f:
                db = yaml.load(f)

            host = db["host"]
            database = ifin("dbname", db, "")
            sqltype = ifin("type", db, sqltype)
            port = db["port"]

        engine_string = "{sqltype}://{username}:{password}@{host}:{port}/{database}"
        engine_string = engine_string.format(sqltype=sqltype, username=username,
                                             password=password, host=host, port=port, database=database)

    conn = sqlalchemy.create_engine(engine_string)

    return conn


def get_session(engine=None, engine_string=None):
    """

    Args:
        engine_string: SQLAlchemy connection string in the form of:

            "{sqltype}://{username}:{password}@{host}:{port}/{database}"

    Returns:
        SQLAlchemy session
    """

    if engine is None and engine_string is None:
        return ValueError("`engine` or `engine_string` must be provided")
    elif engine is None:
        engine = create_connection(engine_string=engine_string)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


Base = declarative_base()


class train_pubg(Base):
    """ Defines the data model for the table `train_pubg`. """

    __tablename__ = 'train_pubg'

    Id = Column(String(100), primary_key=True, unique=True, nullable=False)
    groupId = Column(String(100), unique=False, nullable=False)
    matchId = Column(String(100), unique=False, nullable=False)
    assists = Column(Integer, unique=False, nullable=False)
    boosts = Column(Integer, unique=False, nullable=False)
    damageDealt = Column(Integer, unique=False, nullable=False)  # float
    DBNOs = Column(Integer, unique=False, nullable=False)
    headshotKills = Column(Integer, unique=False, nullable=False)
    heals = Column(Integer, unique=False, nullable=False)
    killPlace = Column(Integer, unique=False, nullable=False)
    killPointsElo = Column(Integer, unique=False, nullable=False)
    kills = Column(Integer, unique=False, nullable=False)
    killStreaks = Column(Integer, unique=False, nullable=False)
    longestKill = Column(Integer, unique=False, nullable=False)  # float
    matchDuration = Column(Integer, unique=False, nullable=False)
    matchType = Column(String(100), unique=False, nullable=False)
    maxPlace = Column(Integer, unique=False, nullable=False)
    numGroups = Column(Integer, unique=False, nullable=False)
    rankPointsElo = Column(Integer, unique=False, nullable=False)
    revives = Column(Integer, unique=False, nullable=False)
    rideDistance = Column(Integer, unique=False, nullable=False)  # float
    roadKills = Column(Integer, unique=False, nullable=False)
    swimDistance = Column(Integer, unique=False, nullable=False)  # float
    teamKills = Column(Integer, unique=False, nullable=False)
    vehicleDestroys = Column(Integer, unique=False, nullable=False)  # float
    walkDistance = Column(Integer, unique=False, nullable=False)
    weaponsAcquired = Column(Integer, unique=False, nullable=False)
    winPoints = Column(Integer, unique=False, nullable=False)
    winPlacePerc = Column(Integer, unique=False, nullable=False)  # float

    def __repr__(self):
        train_pubg_repr = "<train_pubg(Id='%s', groupId='%s', matchId='%s', assists='%d', boosts = '%d', damageDealt = '%d', DBNOs = '%d', headshotKills = '%d', heals = '%d', killPlace = '%d', killPointsElo = '%d', kills = '%d', killStreaks = '%d', longestKill = '%d', matchDuration = '%d', matchType = '%s', maxPlace = '%d', numGroups = '%d', rankPointsElo = '%d', revives = '%d', rideDistance = '%d', roadKills = '%d', swimDistance = '%d', teamKills = '%d', vehicleDestroys = '%d', walkDistance = '%d', weaponsAcquired = '%d', winPoints = '%d', winPlacePerc = '%d'>"
        return train_pubg_repr % (
        self.Id, self.groupId, self.matchId, self.assists, self.boosts, self.damageDealt, self.DBNOs,
        self.headshotKills, self.heals, self.killPlace, self.killPointsElo, self.kills, self.killStreaks,
        self.longestKill, self.matchDuration, self.matchType, self.maxPlace, self.numGroups, self.rankPointsElo,
        self.revives, self.rideDistance, self.roadKills, self.swimDistance, self.teamKills, self.vehicleDestroys,
        self.walkDistance, self.weaponsAcquired, self.winPoints, self.winPlacePerc)


def create_db(args):
    """Creates a RDS or a SQLITE database (based on configuration) with train_pubg table
    Returns: None
    """
    dbconfig = src.config.DBCONFIG
    try:
        if dbconfig is not None:
            engine = create_connection(dbconfig=src.config.DBCONFIG, username=args.user, password=args.password)
            print("Creating RDS database")
        else:
            engine = create_connection(engine_string=src.config.SQLALCHEMY_DATABASE_URI)
            print("Creating sqlite database")
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("Import data")
        df = pd.read_csv("https://s3.us-east-2.amazonaws.com/pubg-finish-prediction-app/Data/train_pubg.csv")
        short_df = df[df['matchType'] == 'solo']
        #short_df = short_df.iloc[1:100,:]
        print("Establish connection")
        session = get_session(engine)
        print("Insert data")
        # old_ARIMA_Params = session.query(ARIMA_Params.CURRENCY, ARIMA_Params.P, ARIMA_Params.D, ARIMA_Params.Q)
        # old_ARIMA_Params.delete()
        session.bulk_insert_mappings(train_pubg, short_df.to_dict(orient="records"))
        session.commit()

        print("Database created with tables")
        # with open(src.config.DBCONFIG, "r") as f:
        #     db = yaml.load(f)
        # temp_conn = pymysql.connect(host=db['host'], user=args.user, port=db['port'], passwd=args.password, db=db['dbname'])
        # print("Running Query")
        # temp = pd.read_sql('select count(*) from train_pubg limit 10;', con=temp_conn)
        # print(temp)
    except Exception as e:
        print("error")
        sys.exit(1)
