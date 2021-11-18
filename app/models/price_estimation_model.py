from pydantic import BaseModel
from datetime import datetime


class InputRealEstate(BaseModel):
    x1: str
    x2: int
    x3: float
    x4: int
    x5: str
    x6: str


class ResponsePriceEstimation(BaseModel):
    estimated_price: str
    DateTime: datetime
