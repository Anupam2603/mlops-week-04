import os
import sys
import pandas as pd
import numpy as np
import pickle
import joblib
import pytest
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

import mlflow
import mlflow.pyfunc

TRACKING_SERVER_URI = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:8100")
mlflow.set_tracking_uri(TRACKING_SERVER_URI)
print(f"MLflow tracking URI set to: {TRACKING_SERVER_URI}")
REGISTERED_MODEL_NAME = "iris-classifier-dt"
MODEL_STAGE = "latest" 

def test_model_accuaracy():
    model_uri = f"models:/{REGISTERED_MODEL_NAME}/{MODEL_STAGE}"
    model = mlflow.pyfunc.load_model(model_uri)


    test = pd.read_csv(f"test/data.csv")
    X_test = test[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y_test = test.species

    y_test_prediciton = model.predict(X_test)
    assert metrics.accuracy_score(y_test, y_test_prediciton) >= 0.8, "Model accuracy is less than 0.8 implies the model has been underfitted."
        
