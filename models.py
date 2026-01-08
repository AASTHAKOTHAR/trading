from pydantic import BaseModel, Field
from typing import Optional

class Instrument(BaseModel):
    symbol: str
    exchange: str
    instrumentType: str
    lastTradedPrice: float


class OrderRequest(BaseModel):
    symbol: str
    side: str                  # BUY / SELL
    orderType: str             # MARKET / LIMIT
    quantity: int = Field(..., gt=0)   # quantity > 0
    price: Optional[float] = None      # required for LIMIT
