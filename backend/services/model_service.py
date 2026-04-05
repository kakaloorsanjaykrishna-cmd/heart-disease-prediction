import pickle
import numpy as np

# Load model once
model = pickle.load(open("../ml-model/model.pkl", "rb"))

def predict(data):
    input_data = np.array(data).reshape(1, -1)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "risk_percentage": round(probability * 100, 2)
    }