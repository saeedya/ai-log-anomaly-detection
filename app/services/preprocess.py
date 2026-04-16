import pandas as pd

FEATURE_COLUMNS = ["response_time", "status_code", "request_count"]


def prepare_input_data(
    response_time: float,
    status_code: int,
    request_count: int,
) -> pd.DataFrame:
    data = pd.DataFrame(
        [
            {
                "response_time": float(response_time),
                "status_code": int(status_code),
                "request_count": int(request_count),
            }
        ]
    )

    return data[FEATURE_COLUMNS]