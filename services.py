import uuid
from fastapi import HTTPException
from storage import instruments, orders, trades, holdings


def place_order(order):
    # ----------- Basic Validations -----------
    if order.orderType == "LIMIT" and order.price is None:
        raise HTTPException(
            status_code=400,
            detail="Price is mandatory for LIMIT orders"
        )

    if order.side not in ["BUY", "SELL"]:
        raise HTTPException(
            status_code=400,
            detail="Order side must be BUY or SELL"
        )

    # ----------- Instrument Validation -----------
    if order.symbol not in instruments:
        raise HTTPException(
            status_code=404,
            detail="Instrument not found"
        )

    # ----------- Generate Order ID -----------
    order_id = str(uuid.uuid4())

    # ----------- Market Price Simulation -----------
    market_price = instruments[order.symbol]["lastTradedPrice"]
    executed_price = market_price if order.orderType == "MARKET" else order.price

    # ----------- SELL Validation -----------
    if order.side == "SELL":
        current_qty = holdings.get(order.symbol, {}).get("quantity", 0)
        if current_qty < order.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient quantity for SELL order"
            )

    # ----------- Store Order -----------
    orders[order_id] = {
        "orderId": order_id,
        "symbol": order.symbol,
        "side": order.side,
        "orderType": order.orderType,
        "quantity": order.quantity,
        "price": executed_price,
        "status": "EXECUTED"
    }

    # ----------- Create Trade -----------
    trades.append({
        "tradeId": str(uuid.uuid4()),
        "orderId": order_id,
        "symbol": order.symbol,
        "price": executed_price,
        "quantity": order.quantity
    })

    # ----------- Update Portfolio -----------
    if order.side == "BUY":
        if order.symbol not in holdings:
            holdings[order.symbol] = {
                "quantity": order.quantity,
                "averagePrice": executed_price
            }
        else:
            old_qty = holdings[order.symbol]["quantity"]
            old_avg = holdings[order.symbol]["averagePrice"]

            new_qty = old_qty + order.quantity
            new_avg = ((old_qty * old_avg) + (order.quantity * executed_price)) / new_qty

            holdings[order.symbol]["quantity"] = new_qty
            holdings[order.symbol]["averagePrice"] = new_avg

    else:  # SELL
        holdings[order.symbol]["quantity"] -= order.quantity
        if holdings[order.symbol]["quantity"] == 0:
            del holdings[order.symbol]

    return orders[order_id]
