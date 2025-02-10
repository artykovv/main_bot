from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.bishkek_datetime import BISHKEK_DATETIME

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    user_id = message.from_user.id
    await message.answer(f"Hello, user {user_id}!")