import pandas as pd
import numpy as np

# Number of samples
n = 1000

np.random.seed(42)

data = {
    "age": np.random.randint(29, 77, n),
    "sex": np.random.randint(0, 2, n),
    "cp": np.random.randint(0, 4, n),  # chest pain type
    "trestbps": np.random.randint(90, 180, n),  # blood pressure
    "chol": np.random.randint(150, 350, n),  # cholesterol
    "fbs": np.random.randint(0, 2, n),
    "restecg": np.random.randint(0, 2, n),
    "thalach": np.random.randint(70, 200, n),  # max heart rate
    "exang": np.random.randint(0, 2, n),
    "oldpeak": np.round(np.random.uniform(0.0, 6.0, n), 1),
    "slope": np.random.randint(0, 3, n),
    "ca": np.random.randint(0, 4, n),
    "thal": np.random.randint(0, 3, n),
}

df = pd.DataFrame(data)

# 🎯 Create target based on conditions (logic-based)
df["target"] = (
    (df["age"] > 50).astype(int) +
    (df["chol"] > 240).astype(int) +
    (df["trestbps"] > 140).astype(int) +
    (df["thalach"] < 120).astype(int) +
    (df["exang"] == 1).astype(int)
)

# Normalize target to 0 or 1
df["target"] = (df["target"] >= 2).astype(int)

# Save dataset
df.to_csv("dataset/heart.csv", index=False)

print("✅ Dataset generated successfully: dataset/heart.csv")