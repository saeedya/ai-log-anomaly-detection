# Custom Metrics Autoscaling

This project includes a custom-metrics-based autoscaling example for Kubernetes.

## Goal

Scale the application based on application-level metrics instead of CPU only.

## Example metric

- `app_requests_per_second`

## Required components

To use custom metrics autoscaling in a real Kubernetes cluster, the following components are required:

- Prometheus
- Prometheus Adapter
- metrics-server

## Flow

Application metrics → Prometheus → Prometheus Adapter → Kubernetes HPA → Deployment scaling

## Notes

This repository includes example manifests and Helm templates for custom-metric-based autoscaling, but a real cluster integration requires Prometheus Adapter configuration.