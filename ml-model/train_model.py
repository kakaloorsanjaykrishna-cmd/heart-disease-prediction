import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("dataset/heart.csv")

# Features & target
X = df.drop("target", axis=1)
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model (better than logistic regression 🔥)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎉 Model saved as model.pkl")