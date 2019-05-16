"""This module can be used to create PUBG database in SQLlite

To create a database in SQLlite:
    Ru n in cmd -`python create_database_rds.py`
"""

import sqlalchemy
import config
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


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

class test_pubg(Base):
    """ Defines the data model for the table `test_pubg`. """

    __tablename__ = 'test_pubg'

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

    def __repr__(self):
        test_pubg_repr = "<test_pubg(Id='%s', groupId='%s', matchId='%s', assists='%d', boosts = '%d', damageDealt = '%d', DBNOs = '%d', headshotKills = '%d', heals = '%d', killPlace = '%d', killPointsElo = '%d', kills = '%d', killStreaks = '%d', longestKill = '%d', matchDuration = '%d', matchType = '%s', maxPlace = '%d', numGroups = '%d', rankPointsElo = '%d', revives = '%d', rideDistance = '%d', roadKills = '%d', swimDistance = '%d', teamKills = '%d', vehicleDestroys = '%d', walkDistance = '%d', weaponsAcquired = '%d', winPoints = '%d', winPlacePerc = '%d'>"
        return test_pubg_repr % (
        self.Id, self.groupId, self.matchId, self.assists, self.boosts, self.damageDealt, self.DBNOs,
        self.headshotKills, self.heals, self.killPlace, self.killPointsElo, self.kills, self.killStreaks,
        self.longestKill, self.matchDuration, self.matchType, self.maxPlace, self.numGroups, self.rankPointsElo,
        self.revives, self.rideDistance, self.roadKills, self.swimDistance, self.teamKills, self.vehicleDestroys,
        self.walkDistance, self.weaponsAcquired, self.winPoints, self.winPlacePerc)


def create_db():
    """Creates a RDS or a SQLITE database (based on configuration) with train_pubg table
    Returns: None
    """
    engine = sqlalchemy.create_engine(config.SQLALCHEMY_DATABASE_URI)
    print("Creating sqlite database")

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database created with tables")


create_db()