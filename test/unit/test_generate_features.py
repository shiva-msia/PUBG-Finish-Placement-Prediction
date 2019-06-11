import pandas as pd
import os
import sys
sys.path.append(os.path.join('../../'))
from sklearn.model_selection import train_test_split
from src.generate_features import generate_features


predictor = pd.DataFrame({'boost': [4, 20, 8, 6, 7, 5, 6, 8, 4, 7],
                          'kills': [8, 5, 0, 2, 0, 4, 7, 5, 6, 2],
                          'weapons': [4, 6, 2, 3, 5, 2, 6, 2, 4, 4],
                          'winPlacePerc': [20, 8, 32, 16, 3, 2, 56, 62, 66, 70]})

response = pd.DataFrame({'winPlacePerc': [20, 8, 32, 16, 3, 2, 56, 62, 66, 70]})


def test_generate_features():
    X_train, X_test, y_train, y_test = train_test_split(predictor.drop(['winPlacePerc'], axis=1), response, test_size=0.3)
    X_tr, X_te, y_tr, y_te = generate_features(predictor, ['boost', 'kills', 'weapons', 'winPlacePerc'])
    assert X_train.shape == X_tr.shape
    assert X_test.shape == X_te.shape
    assert y_train.size == y_tr.size
    assert y_test.size == y_te.size
