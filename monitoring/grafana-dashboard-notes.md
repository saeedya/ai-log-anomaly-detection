# Grafana Dashboard Notes

## Suggested Panels

### 1. Total Request Count
Metric:
- `app_requests_total`

Suggested visualization:
- Time series
- Breakdown by `method` and `endpoint`

### 2. Request Latency
Metric:
- `app_request_duration_seconds`

Suggested visualization:
- Histogram / heatmap
- Percentiles (p50, p95, p99)

### 3. Prediction Volume
Metric:
- `model_predictions_total`

Suggested visualization:
- Time series
- Group by `label`

### 4. Health Monitoring
Use:
- `/health`
- `model_loaded` status via health checks and deployment probes

## Suggested Dashboard Title
AI Log Anomaly Detection Observability Dashboard