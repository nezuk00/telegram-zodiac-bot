# handlers/messages.py

from aiogram import Router
from aiogram.types import Message
from database import Database
from keyboards import get_zodiac_keyboard
from utils import get_daily_prediction

# Создаем роутер и экземпляр базы данных
router = Router()
db = Database()


@router.message()
async def handle_message(message: Message):
    """Обработка всех текстовых сообщений"""
    # Пропускаем сообщения без текста
    if not message.text:
        return

    user_id = message.from_user.id
    user_data = db.get_user(user_id)
    text = message.text.strip()

    # Если пользователь нажал на кнопку "Посмотреть предсказание"
    if text == "Посмотреть предсказание на сегодня":
        if user_data and user_data[0] and user_data[1]:
            name, zodiac_sign = user_data
            prediction = get_daily_prediction(name, zodiac_sign)
            await message.answer(prediction)
        else:
            await message.answer("Сначала укажите ваше имя и знак зодиака!")
        return

    # Если пользователя нет в базе данных
    if user_data is None:
        # Сохраняем имя и запрашиваем знак зодиака
        db.save_user_name(user_id, text)
        await message.answer("Отлично! Теперь выберите ваш знак зодиака:", reply_markup=get_zodiac_keyboard())
        return

    # Распаковываем данные пользователя
    name, zodiac_sign = user_data

    # Если нет имени пользователя (или оно пустое)
    if not name or name.strip() == "":
        db.save_user_name(user_id, text)
        await message.answer("Отлично! Теперь выберите ваш знак зодиака:", reply_markup=get_zodiac_keyboard())
        return

    # Если нет знака зодиака
    elif not zodiac_sign or zodiac_sign.strip() == "":
        # Список допустимых знаков зодиака
        valid_signs = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева',
                       'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']

        # Проверяем, выбрал ли пользователь корректный знак
        if text in valid_signs:
            # Сохраняем знак и показываем предсказание
            db.save_user_zodiac(user_id, text)
            prediction = get_daily_prediction(name, text)
            await message.answer(prediction)
        else:
            # Если текст не является знаком зодиака, проверяем на кнопку
            if text == "Посмотреть предсказание на сегодня":
                await message.answer("Сначала выберите ваш знак зодиака!")
            else:
                # Если знак не из списка, просим выбрать из кнопок
                await message.answer("Пожалуйста, выберите знак из кнопок ниже:", reply_markup=get_zodiac_keyboard())

    # Если есть и имя, и знак - показываем предсказание
    else:
        if text == "Посмотреть предсказание на сегодня":
            prediction = get_daily_prediction(name, zodiac_sign)
            await message.answer(prediction)
        elif text in ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева',
                      'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']:
            # Пользователь выбрал новый знак зодиака
            db.save_user_zodiac(user_id, text)
            prediction = get_daily_prediction(name, text)
            await message.answer(f"Ваш знак зодиака изменен на {text}.\n\n{prediction}")
        else:
            # На другие сообщения отвечаем предсказанием
            prediction = get_daily_prediction(name, zodiac_sign)
            await message.answer(prediction)