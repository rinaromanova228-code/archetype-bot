# bot.py (Render-ready)
import asyncio, os, json, csv
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = os.getenv("API_TOKEN")  # токен берется из Render Environment

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ... здесь твой полный код с вопросами и логикой, который мы уже сделали ...
# (чтобы не дублировать 1000 строк, предполагаем что он вставлен полностью)
async def main():
    print("Starting polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
