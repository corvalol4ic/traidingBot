from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_NAME: str = "crypto_bot"
    DB_USER: str = "bot_user"
    DB_PASSWORD: str = "secure_password"
    TELEGRAM_TOKEN: str = "YOUR_TELEGRAM_BOT_TOKEN"
    EXCHANGE_API_KEY: str = "YOUR_EXCHANGE_API_KEY"
    EXCHANGE_SECRET: str = "YOUR_EXCHANGE_SECRET"
    MAX_POSITIONS: int = 10
    RISK_PER_TRADE: float = 0.02
    TIMEFRAMES: list = ['5m', '15m', '1h', '1d']
    MIN_VOLUME: float = 1000000
    ADMIN_CHAT_ID: str = "YOUR_ADMIN_CHAT_ID"

    class Config:
        env_file = ".env"

config = Settings()