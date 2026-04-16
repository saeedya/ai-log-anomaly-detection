from app.services.preprocess import FEATURE_COLUMNS, prepare_input_data


def test_prepare_input_data_returns_dataframe_with_expected_columns():
    df = prepare_input_data(
        response_time=120.5,
        status_code=200,
        request_count=15,
    )

    assert list(df.columns) == FEATURE_COLUMNS
    assert df.shape == (1, 3)


def test_prepare_input_data_returns_expected_values():
    df = prepare_input_data(
        response_time=250.0,
        status_code=500,
        request_count=42,
    )

    row = df.iloc[0]

    assert row["response_time"] == 250.0
    assert row["status_code"] == 500
    assert row["request_count"] == 42