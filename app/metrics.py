from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests received",
    ["method", "endpoint"],
)

PREDICTION_COUNT = Counter(
    "model_predictions_total",
    "Total number of model predictions made",
    ["label"],
)

REQUEST_LATENCY = Histogram(
    "app_request_duration_seconds",
    "Request latency in seconds",
    ["method", "endpoint"],
)

ERROR_COUNT = Counter(
    "app_errors_total",
    "Total number of application errors",
    ["endpoint"],
)