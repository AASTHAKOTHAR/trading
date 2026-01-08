import requests


class TradingClient:
    """
    Wrapper SDK for Trading APIs.
    This class abstracts REST API calls into simple Python methods.
    """

    def __init__(self, base_url: str):
        """
        Initialize the TradingClient with base API URL
        Example: http://127.0.0.1:8000
        """
        self.base_url = base_url.rstrip("/")

    # ------------------ Instruments ------------------

    def get_instruments(self):
        """
        Fetch list of tradable instruments
        """
        response = requests.get(
            f"{self.base_url}/api/v1/instruments"
        )
        response.raise_for_status()
        return response.json()

    # ------------------ Orders ------------------

    def place_order(
        self,
        symbol: str,
        side: str,
        quantity: int,
        order_type: str,
        price: float = None
    ):
        """
        Place a BUY or SELL order

        :param symbol: Stock symbol (e.g., TCS)
        :param side: BUY or SELL
        :param quantity: Quantity (> 0)
        :param order_type: MARKET or LIMIT
        :param price: Required only for LIMIT orders
        """
        payload = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "orderType": order_type
        }

        if price is not None:
            payload["price"] = price

        response = requests.post(
            f"{self.base_url}/api/v1/orders",
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def get_order_status(self, order_id: str):
        """
        Fetch order status by order ID
        """
        response = requests.get(
            f"{self.base_url}/api/v1/orders/{order_id}"
        )
        response.raise_for_status()
        return response.json()

    # ------------------ Trades ------------------

    def get_trades(self):
        """
        Fetch executed trades
        """
        response = requests.get(
            f"{self.base_url}/api/v1/trades"
        )
        response.raise_for_status()
        return response.json()

    # ------------------ Portfolio ------------------

    def get_portfolio(self):
        """
        Fetch current portfolio holdings
        """
        response = requests.get(
            f"{self.base_url}/api/v1/portfolio"
        )
        response.raise_for_status()
        return response.json()
