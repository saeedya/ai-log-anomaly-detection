from pydantic import BaseModel, Field


class LogFeatures(BaseModel):
    response_time: float = Field(..., ge=0, le=100000)
    status_code: int = Field(..., ge=100, le=599)
    request_count: int = Field(..., ge=0, le=100000)