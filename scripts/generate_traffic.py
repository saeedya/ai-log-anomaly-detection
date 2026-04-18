import os
import random
import time

import requests

PREDICT_URL = os.getenv("PREDICT_URL", "http://127.0.0.1:8000/predict")
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", 2))


def generate_normal_payload() -> dict[str, int]:
    return {
        "response_time": random.randint(80, 200),
        "status_code": random.choice([200, 200, 200, 201]),
        "request_count": random.randint(5, 30),
    }


def generate_anomaly_payload() -> dict[str, int]:
    return {
        "response_time": random.randint(2000, 8000),
        "status_code": random.choice([500, 502, 503]),
        "request_count": random.randint(100, 400),
    }


def main() -> None:
    print("Starting traffic generator... Press Ctrl+C to stop.")

    while True:
        is_anomaly = random.random() < 0.2
        payload = generate_anomaly_payload() if is_anomaly else generate_normal_payload()

        try:
            response = requests.post(PREDICT_URL, json=payload, timeout=5)
            traffic_type = "ANOMALY" if is_anomaly else "NORMAL"
            print(
                f"[{traffic_type}] "
                f"status={response.status_code} | "
                f"payload={payload} | "
                f"response={response.text}"
            )
        except requests.RequestException as exc:
            print(f"Request failed: {exc}")

        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    main()