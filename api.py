import os
import mlflow
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Set the MLflow tracking URI.
# This will use the environment variable 'MLFLOW_TRACKING_URI' if it's set.
# If not, it defaults to your local VM's server.
TRACKING_SERVER_URI = "http://34.55.159.211:8100/"
mlflow.set_tracking_uri(TRACKING_SERVER_URI)

# Define the model we want to load from the registry
REGISTERED_MODEL_NAME = "iris-classifier-dt"
MODEL_STAGE = "latest" # This will grab the newest model

# Load the model from the MLflow Model Registry
try:
    model_uri = f"models:/{REGISTERED_MODEL_NAME}/{MODEL_STAGE}"
    model = mlflow.pyfunc.load_model(model_uri)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    # If the app can't load the model, it should exit.
    exit()

    # Create a FastAPI app instance
app = FastAPI(title="Iris Model Prediction API")

# Define the input data model using Pydantic
# This ensures the input data is valid.
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    
# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": f"Welcome! The '{REGISTERED_MODEL_NAME}"}

# Define the prediction endpoint
@app.post("/predict")
def predict_species(features: IrisFeatures):
    """
    Receives Iris features and returns the predicted species.
    """
    # Convert the input data to a Pandas DataFrame
    # The model was trained on a DataFrame, so it expects one as input.
    input_data = {
        "sepal_length": [features.sepal_length],
        "sepal_width": [features.sepal_width],
        "petal_length": [features.petal_length],
        "petal_width": [features.petal_width]
    }
    input_df = pd.DataFrame(input_data)
            
    # Make a prediction
    try:
        prediction = model.predict(input_df)
        
        # The model returns an array, so get the first element
        predicted_species = prediction[0]
        
        return {
            "predicted_species": predicted_species,
            "input_features": features.dict()
        }
    except Exception as e:
        return {"error": f"Failed to make prediction: {e}"}
