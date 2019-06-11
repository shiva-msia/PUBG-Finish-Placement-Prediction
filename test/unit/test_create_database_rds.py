import pandas as pd
import os
import sys
sys.path.append(os.path.join('../../'))


def test_generate_features():
    df = pd.read_csv("https://s3.us-east-2.amazonaws.com/pubg-finish-prediction-app/Data/train_pubg.csv")
    assert df.empty == False
