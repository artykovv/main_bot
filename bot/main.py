from aiogram import Bot, Dispatcher
from config.config import BOT_TOKEN

from bot.routers.start.router import router as start_router

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start_router)