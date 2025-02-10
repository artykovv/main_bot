import logging
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from bot.routers.notification.router import send_day_notification, send_end_month_notification

from bot.main import bot

logger = logging.getLogger(__name__)


async def setup_scheduler():
    """Настройка планировщика"""
    scheduler = AsyncIOScheduler(timezone=pytz.timezone('Asia/Bishkek'))

    scheduler.add_job(
        send_day_notification,
        trigger=CronTrigger(day="*", hour=12),
        id="day_task",
        replace_existing=True,
    )

    scheduler.add_job(
        send_end_month_notification,
        trigger=CronTrigger(day="last", hour="23, 0"),
        id="end_month_task",
        replace_existing=True,
    )


    logger.info("✅ Планировщик запущен")
    scheduler.start()
    return scheduler