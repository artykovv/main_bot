import asyncio
import logging
from bot.main import start_bot
from api.main import run_api
from backend.schedulers.task import setup_scheduler

logger = logging.getLogger(__name__)


async def main():
    scheduler = await setup_scheduler(),
    await asyncio.gather(
        start_bot(),
        run_api(),  # Запускаем uvicorn в отдельном процессе
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())