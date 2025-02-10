import asyncio
import logging
from bot.main import bot, dp
from backend.schedulers.task import setup_scheduler

logger = logging.getLogger(__name__)


async def start_bot():
    await dp.start_polling(bot)


async def main():
    scheduler = await setup_scheduler()
    logger.info("✅ Планировщик уведомлений запущен")
    
    await start_bot()  


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())