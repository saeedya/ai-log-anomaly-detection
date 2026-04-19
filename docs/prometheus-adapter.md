# Prometheus Adapter Integration

This project includes an example of custom-metrics-based autoscaling.

To make it fully functional in a Kubernetes cluster, Prometheus Adapter is required.

## What is Prometheus Adapter?

Prometheus Adapter exposes Prometheus metrics to Kubernetes via the Custom Metrics API:

custom.metrics.k8s.io

This allows Horizontal Pod Autoscaler (HPA) to scale workloads based on application-level metrics.

## Architecture

Application → Prometheus → Prometheus Adapter → HPA → Deployment

## Example Metric

app_requests_total

Converted into:

rate(app_requests_total[1m])

## Example Adapter Configuration

```yaml
rules:
  - seriesQuery: 'app_requests_total'
    resources:
      overrides:
        namespace: {resource: "namespace"}
        pod: {resource: "pod"}
    name:
      matches: "app_requests_total"
      as: "app_requests_per_second"
    metricsQuery: 'rate(app_requests_total[1m])'
```

## Requirements

- Kubernetes cluster
- Prometheus deployed
- Prometheus Adapter installed
- metrics-server installed