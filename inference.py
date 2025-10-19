import sys
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

def inference():
    with open("./models/model.joblib", 'rb') as f:
        model = joblib.load(f)


    test = pd.read_csv(f"data/data.csv")
    X_test = test[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y_test = test.species

    y_test_prediciton = model.predict(X_test)

    with open("output.txt", 'w') as f:
        print(metrics.accuracy_score(y_test, y_test_prediciton))
        f.write(f"The accuracy score on training data, trained on {sys.argv[1]} versioin of dataset, is {str(metrics.accuracy_score(y_test, y_test_prediciton))}")

if __name__ == "__main__":
    inference()