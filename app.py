
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
import joblib
import pandas as pd

app = FastAPI(title="Breast Cancer Prediction API")

model = joblib.load("models/breast_cancer_model.joblib")
feature_names = joblib.load("models/feature_names.joblib")


class PredictionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    features: dict[str, float]


@app.get("/")
def home():
    return {"message": "Breast Cancer Prediction API is running"}


@app.post("/predict")
def predict(data: PredictionInput):
    if set(data.features.keys()) != set(feature_names):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=422,
            detail="Provide exactly the feature names used during training."
        )

    input_df = pd.DataFrame(
        [[data.features[name] for name in feature_names]],
        columns=feature_names
    )

    prediction = model.predict(input_df)[0]

    return {
        "prediction": str(prediction),
        "meaning": (
            "Malignant" if prediction == "M" else "Benign"
        )
    }
