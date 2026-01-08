
# Trading API – Bajaj Broking Assignment

## Tech Stack
- Python
- FastAPI
- In-memory storage (dict, list)

## How to Run
1. pip install fastapi uvicorn requests
2. uvicorn main:app --reload
3. Open http://127.0.0.1:8000/docs

## APIs
- GET /api/v1/instruments
- POST /api/v1/orders
- GET /api/v1/orders/{orderId}
- GET /api/v1/trades
- GET /api/v1/portfolio

## Assumptions
- Single mocked user
- Market orders executed immediately
- Prices taken from instrument list

## Wrapper SDK
- TradingClient class abstracts REST calls

## Sample Usage
(mention Swagger or SDK examples)
