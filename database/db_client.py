import logging
from typing import List, Dict, Optional
from datetime import datetime
import asyncpg
from config.settings import config

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            host=config.DB_HOST,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD
        )
        logger.info("Connected to database")

    async def get_candles(self, symbol: str, timeframe: str, limit: int = 500) -> List[Dict]:
        async with self.pool.acquire() as conn:
            return await conn.fetch(
                "SELECT * FROM candles WHERE symbol = $1 AND timeframe = $2 ORDER BY timestamp DESC LIMIT $3",
                symbol, timeframe, limit
            )

    async def get_active_pairs(self) -> List[str]:
        async with self.pool.acquire() as conn:
            return await conn.fetch(
                "SELECT symbol FROM pair_metrics WHERE volume_24h > $1 ORDER BY volume_24h DESC LIMIT 50",
                config.MIN_VOLUME
            )

    async def save_position(self, position: Dict):
        async with self.pool.acquire() as conn:
            await conn.execute(
                """INSERT INTO positions 
                (pair, timeframe, side, entry_price, size, opened_at, status, order_id)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8)""",
                position['pair'], position['timeframe'], position['side'],
                position['entry_price'], position['size'], position['opened_at'],
                position['status'], position.get('order_id')
            )