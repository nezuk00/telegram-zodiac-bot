# handlers/commands.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from database import Database
from keyboards import get_zodiac_keyboard
from utils import get_daily_prediction

# Создаем роутер и экземпляр базы данных
router = Router()
db = Database()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обработка команды /start"""
    user_id = message.from_user.id
    user_data = db.get_user(user_id)

    # Если пользователя нет в базе данных
    if user_data is None:
        # Создаем новую запись
        db.save_user_name(user_id, "")
        await message.answer("Привет! Как тебя зовут?")
        return

    # Распаковываем данные пользователя
    name, zodiac_sign = user_data

    # Если имя пустое или None
    if not name or name.strip() == "":
        await message.answer("Привет! Как тебя зовут?")
        return

    # Если знак зодиака пустой или None
    if not zodiac_sign or zodiac_sign.strip() == "":
        await message.answer("Отлично! Теперь выберите ваш знак зодиака:", reply_markup=get_zodiac_keyboard())
        return

    # Если есть и имя, и знак - показываем предсказание
    prediction = get_daily_prediction(name, zodiac_sign)
    await message.answer(prediction)