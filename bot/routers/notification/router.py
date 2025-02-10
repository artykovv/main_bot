from asyncio.log import logger
from bot.main import bot
from config.config import MY_CHAT_ID
from datetime import datetime, timedelta
import pytz



async def send_day_notification():
    """Функция отправки уведомления каждый день"""
    try:
        utc_now = datetime.now(pytz.utc)
        bishkek_now = utc_now.astimezone(pytz.timezone('Asia/Bishkek'))

        # Calculate days remaining until the end of the month
        next_month = bishkek_now.replace(day=28) + timedelta(days=4)
        last_day_of_month = next_month - timedelta(days=next_month.day)
        days_remaining = (last_day_of_month - bishkek_now).days

        data = (
            f"🔔 Ежедневное уведомление!\n"
            f"UTC: {utc_now}\n"
            f"Bishkek: {bishkek_now}\n\n"
            f"До конца месяца осталось: {days_remaining} дней"
        )

        await bot.send_message(chat_id=MY_CHAT_ID, text=data)
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления: {e}")


async def send_end_month_notification():
    """Функция отправки уведомления в конце месяца"""
    try:
        utc_now = datetime.now(pytz.utc)
        bishkek_now = utc_now.astimezone(pytz.timezone('Asia/Bishkek'))

        data = (
            f"🔔 Уведомление в конце месяца!!\n"
            f"UTC: {utc_now}\n"
            f"Bishkek: {bishkek_now}"
        )

        await bot.send_message(chat_id=MY_CHAT_ID, text=data)
        await bot.send_message(chat_id=MY_CHAT_ID, text="seiko binar надо запустить")
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления: {e}")