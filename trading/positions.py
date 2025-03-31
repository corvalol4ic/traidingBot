from typing import Dict
from datetime import datetime
from config.settings import config

class PositionManager:
    def __init__(self):
        self.positions = {}

    async def can_open_position(self, pair: str, signal: str, timeframe: str) -> bool:
        if len(self.positions) >= config.MAX_POSITIONS:
            return False
        if pair in self.positions:
            return False
        if timeframe not in ['1h', '1d']:
            return False
        return True

    async def open_position(self, position: Dict):
        self.positions[position['pair']] = position