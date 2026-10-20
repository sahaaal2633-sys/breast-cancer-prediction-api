# MLOps Assignment 10: Breast Cancer Prediction API

## 1. Project Overview

This project demonstrates how to deploy a Machine Learning model using FastAPI and Docker. The model predicts whether a breast cancer tumor is malignant or benign based on numerical features.

The project covers model serving, REST API development, containerization, API testing, and model monitoring planning.

## 2. Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- Uvicorn
- Docker
- Requests
- Git and GitHub

## 3. Project Structure

## Project Structure

```text
breast-cancer-prediction-api/
├── app.py
├── test_api.py
├── data.csv
├── Dockerfile
├── requirements.txt
├── Readme.md
├── monitoring_plan.md
├── Assignment 10.ipynb
└── models/
    ├── breast_cancer_model.joblib
    └── feature_names.joblib
```


## 4. Model Description

The project uses a trained machine learning classification model to predict breast cancer diagnosis.

- **M — Malignant:** The model predicts a malignant tumor.
- **B — Benign:** The model predicts a benign tumor.

The API receives numerical features and returns the model's prediction.

## 5. API Development

FastAPI is used to create a REST API for serving predictions.

### Prediction Endpoint

- **Method:** POST
- **Endpoint:** `/predict`
- **Purpose:** Accept input features and return a prediction.

FastAPI also provides interactive API documentation at `/docs`.

## 6. Running the Project with Docker

Build the Docker image:

```bash
docker build -t breast-cancer-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 breast-cancer-api
```

Once the container starts, the API is available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Keep the container running while testing the API.

## 7. Testing the API

The `test_api.py` script loads sample data from `data.csv`, sends input features to the `/predict` endpoint, and displays the API response.

Run the test script in a separate terminal:

```bash
python3 test_api.py
```

A successful request returns HTTP status code `200` and the prediction result.

## 8. Model Monitoring Plan

The monitoring plan covers:

- **API availability:** Check whether the API is running and responding.
- **Request monitoring:** Track successful requests and errors.
- **Prediction monitoring:** Record prediction outputs and response times.
- **Data drift:** Monitor changes in incoming feature distributions.
- **Model performance:** Evaluate predictions against actual outcomes when labels become available.
- **Retraining:** Consider retraining when data drift or declining model performance is detected.

These are proposed monitoring activities and should be implemented or measured as part of a monitoring system if required.

## 9. Conclusion

This project demonstrates how to serve a machine learning model through a REST API, package the application using Docker, test predictions using Python, and define a monitoring strategy for production use.

The project provides a foundation for learning practical MLOps deployment workflows.
