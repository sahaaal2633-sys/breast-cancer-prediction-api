
import pandas as pd
import requests

# API endpoint
url = "http://127.0.0.1:8000/predict"

# Load dataset
df = pd.read_csv("data.csv")

# Remove unnecessary columns
df = df.drop(columns=["Unnamed: 32", "id"], errors="ignore")

# Separate input features from target
X = df.drop(columns=["diagnosis"])

# Select one row
features = X.iloc[0].to_dict()

# Convert values to Python floats
features = {key: float(value) for key, value in features.items()}

# Display number of features
print("Number of features:", len(features))

# Send request to API
response = requests.post(
    url,
    json={"features": features}
)

# Display result
print("Status code:", response.status_code)
print("Response:", response.text)
