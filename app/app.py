from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load the brain we made in Phase 1
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: dict):
    # User sends: {"features": [8, 307, 3504, 12]}
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return {"mpg_prediction": float(prediction[0])}