import sys
import pandas as pd
import numpy as np
import pickle
import joblib
import pytest
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

def test_model_accuaracy():
    with open("models/model.joblib", 'rb') as f:
        model = joblib.load(f)


    test = pd.read_csv(f"test/data.csv")
    X_test = test[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y_test = test.species

    y_test_prediciton = model.predict(X_test)

    with open("output.txt", 'w') as f:       
        assert metrics.accuracy_score(y_test, y_test_prediciton) < 1.0, "Model accuracy is less than 1 implies the model has not been overfitted."
        
