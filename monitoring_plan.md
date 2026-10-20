# Model Monitoring Plan — Breast Cancer Prediction API

## 1. Project Overview

This project deploys a Random Forest classification model using FastAPI and Docker. The API accepts 30 numerical features and returns a prediction of malignant (M) or benign (B).

## 2. Monitoring Objectives

- Ensure the API remains available.
- Monitor response time and request failures.
- Validate incoming data.
- Detect changes in input data (data drift).
- Evaluate model performance when actual labels become available.

## 3. Monitoring Metrics

| Metric | What to Monitor | Example Alert Condition |
|---|---|---|
| API availability | Whether the API responds | API unavailable for 2 consecutive minutes |
| Response latency | Time taken to return a prediction | 95th percentile exceeds 1 second |
| Error rate | Percentage of failed requests | More than 5% errors over 5 minutes |
| Input validation | Missing, invalid, or unexpected features | Repeated invalid requests |
| Data drift | Changes in feature distributions | Drift exceeds a defined statistical threshold |
| Model performance | Precision, recall, and F1-score | Recall falls below the agreed target once labels are available |

These alert thresholds are initial examples and should be adjusted based on observed traffic and operational requirements.

## 4. Monitoring Methods

### API Monitoring
Check the API health endpoint periodically and record response status, latency, and errors.

### Input Data Monitoring
Validate that each request contains all 30 expected features and that values are numerical and finite.

### Data Drift Monitoring
Compare incoming feature distributions with the training data using statistical methods such as the Kolmogorov–Smirnov test or Population Stability Index (PSI).

### Model Performance Monitoring
When verified actual outcomes become available, compare predictions with actual labels and calculate precision, recall, F1-score, and a confusion matrix.

## 5. Logging and Alerts

Record timestamps, request status, latency, model version, and error details. Avoid logging raw health-related input values or identifiable personal information.

Generate alerts for prolonged downtime, increasing error rates, significant data drift, or declining model performance.

## 6. Retraining Strategy

Investigate significant data drift or reduced performance before retraining. Retrain using appropriate, verified, representative data; evaluate the new model against the current version; and deploy it only after it meets the required performance criteria.

Keep model versions and evaluation results for reproducibility and rollback.

## 7. Limitations and Safety

This project is an educational demonstration. Its predictions must not be used for real clinical decisions. A real medical application would require extensive clinical validation, appropriate privacy safeguards, and qualified medical oversight.

## 8. Current Implementation Status

The model is served through FastAPI and packaged in a Docker container. The monitoring activities described above are a proposed plan; automated production monitoring and alerting must be implemented separately before they can be considered operational.