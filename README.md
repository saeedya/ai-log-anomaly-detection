![License](https://img.shields.io/badge/license-educational-blue)

# AI-based Log Anomaly Detection System

![Status](https://img.shields.io/badge/status-in--progress-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![CI](https://github.com/saeedya/ai-log-anomaly-detection/actions/workflows/ci.yaml/badge.svg)

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
- Configuration
- Getting Started
- Kubernetes Deployment
- Helm Deployment
- API Endpoints
- Observability
- Running Tests
- Security Checks
- Upcoming Features

## Overview

This project is an end-to-end AI and MLOps system designed to detect anomalies in application and infrastructure logs using machine learning techniques.

It simulates a real-world production scenario where logs are collected, processed, analyzed, and served through an API.

This project focuses on bridging the gap between machine learning models and production systems through a practical MLOps approach.

---

## Project Status

🚧 In Progress – Core API, preprocessing, model integration, Dockerization, dependency security hardening, CI automation, Kubernetes manifests, Helm chart support, production hardening, and observability integration completed.  
Next phase: deployment refinement and production-grade monitoring enhancements.

---

## Development Workflow

- Feature-based development with Git commits
- Incremental implementation (API → ML → Deployment)
- Unit, API, and security testing at each phase
- Continuous documentation updates
- Separate production and development dependencies
- Linting and security checks for code quality assurance
- Automated CI checks for testing, linting, and security scanning

---

## Security Considerations

- Input validation using Pydantic
- Static code analysis using Bandit
- Dependency vulnerability scanning using pip-audit
- No hardcoded secrets or credentials

---

## Features

* Input preprocessing for structured log features
* Feature preparation for anomaly detection input
* Anomaly detection using machine learning
* REST API built with FastAPI
* Input validation using Pydantic
* Unit, API, and security testing
* Docker support for containerization
* Production-ready Kubernetes deployment with manifests and Helm chart
* Dockerized application for portable execution
* GitHub Actions CI for automated quality and security checks
* Environment-based configuration for runtime settings
* Structured application logging
* Non-root Docker container for improved container security
* Prometheus-compatible metrics endpoint
* Request and prediction observability

---

## Tech Stack

* Python
* FastAPI
* Pandas
* Scikit-learn
* Docker
* Kubernetes
* Pytest
* Bandit
* pip-audit
* Ruff
* Makefile
* GitHub Actions
* Helm
* Prometheus client

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
├── app/                    # FastAPI application
│   ├── config.py           # Environment-based runtime settings
│   ├── logging_config.py   # Logging setup
│   ├── main.py
│   ├── schemas.py
│   └── services/
├── .env.example            # Example environment variables
├── ml/                       # ML training and prediction logic
├── tests/                    # Unit, API, and security tests
├── docs/                     # Project documentation
├── helm/                     # Helm chart for Kubernetes deployment
│   └── ai-log-anomaly-detection/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── k8s/                      # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
├── models/                   # Saved ML models
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development & testing dependencies
├── pytest.ini                # Pytest configuration
├── ruff.toml                 # Linting configuration
├── Dockerfile
├── .dockerignore
├── Makefile                  # Development commands (optional)
└── README.md
```

---

## Configuration

The application supports basic runtime configuration through environment variables.

### Example
```bash
export APP_NAME="AI Log Anomaly Detection API"
export MODEL_PATH="models/isolation_forest.pkl"
export LOG_LEVEL="INFO"

```
Note: You can also copy `.env.example` and adapt the values for your environment.

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
#### Production
```bash
pip install -r requirements.txt
```

#### Development & testing
```bash
pip install -r requirements-dev.txt
```

---

### 4. Train the model
```bash
python ml/train.py
```

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

## Run with Docker

### Build the image
```bash
docker build -t ai-log-anomaly-detection:latest .
```

### Run the container
```bash
docker run --rm -p 8000:8000 ai-log-anomaly-detection:latest
```

---

## Kubernetes Deployment

### Apply Kubernetes manifests
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Verify resources
```bash
kubectl get all -n ai-log-anomaly
```

### Port-forward the service
```bash
kubectl port-forward svc/ai-log-anomaly-detection 8000:80 -n ai-log-anomaly
```

### Access the application
```bash
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

---

## Helm Deployment

### Lint the chart
```bash
helm lint helm/ai-log-anomaly-detection
```

### Render Kubernetes manifests
```bash
helm template ai-log-anomaly-detection helm/ai-log-anomaly-detection
```

### Install the chart
```bash
helm install ai-log-anomaly-detection helm/ai-log-anomaly-detection
```

### Upgrade the release
```bash
helm upgrade ai-log-anomaly-detection helm/ai-log-anomaly-detection
```

### Uninstall the release
```bash
helm uninstall ai-log-anomaly-detection -n ai-log-anomaly
```

---

## API Endpoints

### GET /

Returns basic project info

### GET /health

Returns API health status

### POST /predict
Runs anomaly detection on structured log features using the trained ML model.

### GET /metrics

Exposes Prometheus-compatible application metrics for observability and monitoring.

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

## Observability

The application exposes Prometheus-compatible metrics at:

```bash
GET /metrics
```

### Available metrics

* app_requests_total
* app_request_duration_seconds
* model_predictions_total

---

## Running Tests
### Run all tests

```bash
pytest
```

### Run tests with coverage
```bash
pytest --cov=app --cov=ml
```

### Run lint checks
```bash
ruff check .
```
---

## Security Checks

### Static analysis

```bash
bandit -r app ml
```

### Dependency vulnerabilities

```bash
pip-audit -r requirements.txt
pip-audit -r requirements-dev.txt
```

### Linting

```bash
ruff check .
```

---

## Upcoming Features
- Image registry integration
- Grafana dashboard integration
- Alerting rules for anomaly prediction metrics
- Production-grade deployment refinements

---

## License

This project is for educational and demonstration purposes.

---

## Author

Saeed Yasrebi

---

## Screenshots

### API Documentation (Swagger UI)
![Swagger UI](docs/swagger.png)

### Metrics Endpoint
![Metrics](docs/metrics.png)
