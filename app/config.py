import os


class Settings:
    app_name: str = os.getenv("APP_NAME", "AI Log Anomaly Detection API")
    model_path: str = os.getenv("MODEL_PATH", "models/isolation_forest.pkl")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()