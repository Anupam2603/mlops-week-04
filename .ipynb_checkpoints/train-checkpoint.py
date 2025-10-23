import pandas as pd
import numpy as np
import pickle
import joblib
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
#New libraries
import argparse
import mlflow
import mlflow.sklearn

TRACKING_SERVER_URI = "http://127.0.0.1:8100"
mlflow.set_tracking_uri(TRACKING_SERVER_URI)

def training():
    
    
    # NEW: --- Set up argument parser for hyperparameters ---
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_depth", type=int, default=3, help="Max depth of the decision tree")
    parser.add_argument("--criterion", type=str, default="gini", help="Criterion for split (gini or entropy)")
    parser.add_argument("--exp_name", type=str, default="Iris_Classifier_Experiment", help="Experiment Name")
    args = parser.parse_args()
    
    #Starting a new experiment
    mlflow.set_experiment(args.exp_name)
    with mlflow.start_run() as run:
        print(f"Starting run: {run.info.run_id}")

        # Load data (this assumes you've run dvc pull)
        try:
            df = pd.read_csv('data/data.csv')
        except FileNotFoundError:
            print("Error: 'data/data.csv' not found.")
            print("Please run 'dvc pull' to get the data.")
            return

        # Split data
        X = df.drop('species', axis=1)
        y = df['species']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # NEW: --- Log hyperparameters to MLflow ---
        mlflow.log_param("max_depth", args.max_depth)
        mlflow.log_param("criterion", args.criterion)
        print(f"Parameters: max_depth={args.max_depth}, criterion={args.criterion}")

        # Train model
        model = DecisionTreeClassifier(
            max_depth=args.max_depth,
            criterion=args.criterion
        )
        model.fit(X_train, y_train)

        # Evaluate model
        y_preds = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_preds)

        # NEW: --- Log metrics to MLflow ---
        mlflow.log_metric("accuracy", accuracy)
        print(f"Metrics: accuracy={accuracy}")

        # NEW: --- Log the model to MLflow ---
        # This is the most important part.
        # This REPLACES joblib.dump() and `dvc add model`
        # We are also giving it a "registered_model_name", which
        # puts it in the MLflow Model Registry.
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",  # This is a folder name *inside* the MLflow run
            registered_model_name="iris-classifier-dt" # This is the name in the Model Registry
        )
        print("Model has been logged to MLflow and registered.")

if __name__ == "__main__":
    training()