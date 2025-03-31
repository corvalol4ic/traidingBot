import logging
from typing import Dict
import ccxt.async_support as ccxt
from config.settings import config

logger = logging.getLogger(__name__)

class ExchangeClient:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': config.EXCHANGE_API_KEY,
            'secret': config.EXCHANGE_SECRET,
            'enableRateLimit': True
        })

    async def connect(self):
        await self.exchange.load_markets()
        logger.info("Connected to exchange")

    async def get_price(self, symbol: str) -> float:
        ticker = await self.exchange.fetch_ticker(symbol)
        return float(ticker['last'])

    async def create_order(self, symbol: str, side: str, amount: float) -> Dict:
        order = await self.exchange.create_order(
            symbol=symbol,
            type='market',
            side=side,
            amount=amount
        )
        logger.info(f"Order created: {order}")
        return order