from fastapi import FastAPI
from models import OrderRequest
from storage import instruments, orders, trades, holdings
from services import place_order

app = FastAPI(title="Trading API")


# ------------------ Instruments ------------------

@app.get("/api/v1/instruments")
def get_instruments():
    # instruments is a dict → return list of values
    return list(instruments.values())


# ------------------ Orders ------------------

@app.post("/api/v1/orders")
def create_order(order: OrderRequest):
    return place_order(order)


@app.get("/api/v1/orders/{order_id}")
def get_order_status(order_id: str):
    return orders.get(order_id, {"error": "Order not found"})


# ------------------ Trades ------------------

@app.get("/api/v1/trades")
def get_trades():
    return trades


# ------------------ Portfolio ------------------

@app.get("/api/v1/portfolio")
def get_portfolio():
    portfolio = []

    for symbol, data in holdings.items():
        current_price = instruments[symbol]["lastTradedPrice"]

        portfolio.append({
            "symbol": symbol,
            "quantity": data["quantity"],
            "averagePrice": round(data["averagePrice"], 2),
            "currentValue": round(data["quantity"] * current_price, 2)
        })

    return portfolio
