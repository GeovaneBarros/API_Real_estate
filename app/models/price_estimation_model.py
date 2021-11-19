from pydantic import BaseModel
from datetime import datetime


class InputRealEstate(BaseModel):
    x1: str
    x2: float
    x3: float
    x4: int
    x5: float
    x6: float


class ResponsePriceEstimation(BaseModel):
    estimated_price: str
    DateTime: datetime
