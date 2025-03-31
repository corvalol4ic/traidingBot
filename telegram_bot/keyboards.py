from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def get_chart_button(symbol: str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="View Chart",
        url=f"https://www.tradingview.com/chart/?symbol=BINANCE:{symbol}"
    ))
    return builder.as_markup()