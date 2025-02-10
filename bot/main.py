import logging
from aiogram import Bot, Dispatcher
from config.config import BOT_TOKEN, MY_CHAT_ID
from bot.routers.start.router import router as start_router

logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start_router)




async def send_startup_notification():
    """Отправляет сообщение в чат при старте бота"""
    try:
        await bot.send_message(MY_CHAT_ID, "✅ Бот запущен и работает!")
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления о старте: {e}")

async def send_shutdown_notification():
    """Отправляет сообщение в чат перед остановкой бота"""
    try:
        await bot.send_message(MY_CHAT_ID, "⚠️ Бот остановлен!")
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления о выключении: {e}")


async def start_bot():
    """Запуск бота с уведомлением"""
    await send_startup_notification()  # Отправляем уведомление о запуске
    try:
        await dp.start_polling(bot)
    finally:
        await send_shutdown_notification()  # Уведомление при остановке
        await bot.session.close()  # Закрываем сессию бота