from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from trading.analyzer import TradingAnalyzer

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "🚀 <b>Crypto Trading Bot</b>\n\n"
        "<b>Available commands:</b>\n"
        "/positions - Show open positions\n"
        "/analyze [pair] - Analyze specific pair\n"
        "/stats - Show trading statistics\n"
        "/stop - Stop all trading activity",
        parse_mode=ParseMode.HTML
    )

@router.message(Command("positions"))
async def positions_command(message: Message, analyzer: TradingAnalyzer):
    positions_msg = await analyzer.get_positions_message()
    await message.answer(positions_msg, parse_mode=ParseMode.HTML)

@router.message(Command("analyze"))
async def analyze_command(message: Message, analyzer: TradingAnalyzer):
    if not message.text.split()[1:]:
        await message.answer("Please specify a pair, e.g. /analyze BTCUSDT")
        return

    pair = message.text.split()[1].upper()
    await analyzer.analyze_pair(pair)
    await message.answer(f"Analysis completed for {pair}")