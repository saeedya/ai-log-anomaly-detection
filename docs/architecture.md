# System Architecture

## High-Level Flow

Logs → Preprocessing → Feature Engineering → ML Model → FastAPI → Metrics → Client

## Components

- **FastAPI API**
  - Exposes `/predict`, `/health`, and `/metrics`
- **Preprocessing Layer**
  - Validates and transforms structured log features
- **ML Model**
  - Isolation Forest model for anomaly detection
- **Observability**
  - Prometheus-compatible metrics endpoint
- **Containerization & Deployment**
  - Docker, Kubernetes manifests, and Helm chart
- **CI/CD**
  - GitHub Actions for CI, release automation, and container publishing