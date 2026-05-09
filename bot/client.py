import os
import time

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceFuturesClient:

    def __init__(self):

        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Fix timestamp drift
        server_time = self.client.get_server_time()
        system_time = int(time.time() * 1000)

        self.client.timestamp_offset = server_time["serverTime"] - system_time

    def get_client(self):
        return self.client