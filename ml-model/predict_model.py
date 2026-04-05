import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

def predict_heart_disease(data):
    """
    data: list of 13 features
    returns: prediction (0 or 1)
    """
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    
    return int(prediction[0])


# Test (optional)
if __name__ == "__main__":
    sample = [52,1,0,125,212,0,1,168,0,1.0,2,2,3]
    result = predict_heart_disease(sample)
    
    print("⚠️ Risk" if result == 1 else "✅ Safe")