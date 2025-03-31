import asyncio
from aiogram import Bot, Dispatcher
from config.settings import config
from database.db_client import Database
from exchange.api_client import ExchangeClient
from telegram_bot.handlers import router
from trading.analyzer import TradingAnalyzer
from utils.logger import setup_logger


async def main():
    setup_logger()

    # Инициализация компонентов
    db = Database()
    exchange = ExchangeClient()
    analyzer = TradingAnalyzer(db, exchange)

    # Подключение к сервисам
    await db.connect()
    await exchange.connect()

    # Настройка бота
    bot = Bot(token=config.TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    # Запуск задач
    asyncio.create_task(analyzer.start_analysis_loop())

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())