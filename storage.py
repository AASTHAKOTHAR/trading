# In-memory storage (acts like a database)

instruments = {
    "TCS": {
        "symbol": "TCS",
        "exchange": "NSE",
        "instrumentType": "EQ",
        "lastTradedPrice": 3500.0
    },
    "INFY": {
        "symbol": "INFY",
        "exchange": "NSE",
        "instrumentType": "EQ",
        "lastTradedPrice": 1600.0
    }
}

orders = {}     # orderId -> order details
trades = []     # list of executed trades
holdings = {}   # symbol -> { quantity, averagePrice }
