# AI-based Log Anomaly Detection System

![Status](https://img.shields.io/badge/status-in--progress-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)

---

## Table of Contents

- Overview
- Project Status
- Development Workflow
- Security Considerations
- Features
- Tech Stack
- Architecture
- Project Structure
- Getting Started
- API Endpoints
- Running Tests
- Security Checks
- Upcoming Features

## Overview

This project is an end-to-end AI and MLOps system designed to detect anomalies in application and infrastructure logs using machine learning techniques.

It simulates a real-world production scenario where logs are collected, processed, analyzed, and served through an API.

This project focuses on bridging the gap between machine learning models and production systems through a practical MLOps approach.

---

## Project Status

🚧 In Progress – Initial API and project structure completed.  
Next phase: ML model integration and prediction endpoint.

---

## Development Workflow

- Feature-based development with Git commits
- Incremental implementation (API → ML → Deployment)
- Unit, API, and security testing at each phase
- Continuous documentation updates

---

## Security Considerations

- Input validation using Pydantic
- Static code analysis using Bandit
- Dependency vulnerability scanning using pip-audit
- No hardcoded secrets or credentials

---

## Features

* Log ingestion and preprocessing
* Feature extraction from structured log data
* Anomaly detection using machine learning (planned)
* REST API built with FastAPI
* Input validation using Pydantic
* Unit, API, and security testing
* Docker support for containerization
* Prepared for future Kubernetes deployment

---

## Tech Stack

* Python
* FastAPI
* Pandas
* Scikit-learn
* Docker
* Kubernetes (planned)
* Pytest
* Bandit
* pip-audit

---

## Architecture

The system follows a typical MLOps pipeline:

Logs → Preprocessing → Feature Engineering → ML Model → Prediction API → Client

- Logs are collected from applications and infrastructure
- Data is preprocessed and transformed into structured features
- A machine learning model detects anomalies
- Results are served via a REST API

---

## Project Structure

```
ai-log-anomaly-detection/
├── app/            # FastAPI application
│   ├── main.py
│   ├── schemas.py
│   └── services/
├── ml/             # ML training and prediction logic
├── tests/          # Unit, API, and security tests
├── docs/           # Project documentation
├── models/         # Saved ML models
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-log-anomaly-detection
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Train the model (Planned)
Model training functionality will be implemented in the next phase.

---

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

---

### 6. Access API

* http://127.0.0.1:8000
* http://127.0.0.1:8000/docs

---

## API Endpoints

### GET /

Returns basic project info

### GET /health

Returns API health status

### POST /predict (Planned)
Endpoint for detecting anomalies from log features. This will be implemented in the next phase.

#### Example Request

```json
{
  "response_time": 120,
  "status_code": 200,
  "request_count": 15
}
```

#### Example Response

```json
{
  "prediction": 1,
  "label": "normal"
}
```

---

## Running Tests

```bash
pytest
```

### With coverage

```bash
pytest --cov=app --cov=ml
```

---

## Security Checks

### Static analysis

```bash
bandit -r app ml
```

### Dependency vulnerabilities

```bash
pip-audit
```

---

## Upcoming Features
- ML model training using Isolation Forest
- Log preprocessing and feature engineering pipeline
- Integration of ML model with FastAPI
- Docker containerization
- Kubernetes deployment
- CI/CD pipeline with automated testing and security checks

---

## License

This project is for educational and demonstration purposes.

---

## Author

Saeed Yasrebi
