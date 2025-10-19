import pandas as pd
import numpy as np
import pickle
import joblib
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics

def training():
    train = pd.read_csv(f"./data/data.csv")
    X_train, y_train = train[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']], train.species

    dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
    dt.fit(X_train, y_train)

    with open("./models/model.joblib", 'wb') as f:
        joblib.dump(dt, f)

if __name__ == "__main__":
    training()